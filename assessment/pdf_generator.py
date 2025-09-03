import os
from io import BytesIO
from datetime import datetime
import json
from django.template.loader import render_to_string
from django.conf import settings
import tempfile
import subprocess
import platform

class PDFGenerator:
    def __init__(self):
        pass

    def generate_pdf(self, scores, dimensions_data, session_id, user_company='Your Organization'):
        """Generate PDF using HTML templates with real assessment data"""
        # Get real assessment data
        from .models import AssessmentResponse
        assessment = AssessmentResponse()
        actual_scores = assessment.calculate_scores(session_id)
        
        # Use actual category scores from assessment
        dimensions = list(actual_scores['category_scores'].keys())
        client_scores = list(actual_scores['category_scores'].values())
        industry_benchmarks = [2.8, 2.5, 2.7, 2.6, 2.9, 2.4, 2.2, 2.5, 2.3][:len(dimensions)]
        
        total_pages = 3 + len(dimensions)  # Cover + Radar + Dimensions + Next Steps
        
        # Generate HTML pages
        html_pages = []
        
        # Cover page
        cover_html = self.create_cover_page(user_company)
        html_pages.append(cover_html)
        
        # Radar overview page
        radar_html = self.create_radar_overview_page(dimensions, client_scores, industry_benchmarks, total_pages, actual_scores)
        html_pages.append(radar_html)
        
        # Dimension pages - use actual assessment data
        for i, dimension in enumerate(dimensions):
            dimension_html = self.create_dimension_page(
                dimension, dimensions_data.get(dimension, {}), actual_scores, dimensions, client_scores, 
                industry_benchmarks, i, i+3, total_pages
            )
            html_pages.append(dimension_html)
        
        # Next steps page
        next_steps_html = self.create_next_steps_page(total_pages)
        html_pages.append(next_steps_html)
        
        # Combine all HTML pages with proper page breaks
        combined_html = self.create_combined_html(html_pages)
        
        # Try to convert to PDF using browser automation
        try:
            pdf_buffer = self.html_to_pdf_browser(combined_html, session_id)
            print(f"PDF report generated successfully for session: {session_id}")
            return pdf_buffer
        except Exception as e:
            print(f"Browser PDF generation failed: {e}")
            # Fallback: return HTML content
            buffer = BytesIO(combined_html.encode('utf-8'))
            return buffer

    def create_cover_page(self, company_name):
        """Create cover page using HTML template"""
        context = {
            'company_name': company_name,
            'report_date': datetime.now().strftime("%B %Y")
        }
        return render_to_string('pdf/cover_page.html', context)

    def create_radar_overview_page(self, dimensions, client_scores, industry_benchmarks, total_pages, actual_scores=None):
        """Create radar overview page using HTML template"""
        context = {
            'dimensions': json.dumps(dimensions),
            'client_scores': json.dumps(client_scores),
            'industry_benchmarks': json.dumps(industry_benchmarks),
            'total_pages': total_pages,
            'scores': actual_scores or {}
        }
        return render_to_string('pdf/radar_overview.html', context)

    def create_dimension_page(self, dimension_name, dimension_data, scores, dimensions, client_scores, industry_benchmarks, dimension_index, page_number, total_pages):
        """Create dimension detail page using HTML template"""
        score = scores['category_scores'].get(dimension_name, 0)
        stage = self.get_stage_from_score(score)
        stage_guidance = self.get_stage_guidance(dimension_name, stage)
        
        # Calculate total score and stage range points
        total_score = int(score * 5)
        stage_ranges = {
            'Nascent': {'min': 5, 'max': 9, 'avgMin': 1.0, 'avgMax': 1.9},
            'Emerging': {'min': 10, 'max': 12, 'avgMin': 2.0, 'avgMax': 2.4},
            'Scaling': {'min': 13, 'max': 17, 'avgMin': 2.5, 'avgMax': 3.4},
            'Transforming': {'min': 18, 'max': 21, 'avgMin': 3.5, 'avgMax': 4.2},
            'Leading': {'min': 22, 'max': 25, 'avgMin': 4.3, 'avgMax': 5.0}
        }
        
        stage_range_data = stage_ranges.get(stage, stage_ranges['Nascent'])
        stage_range_points = f"{stage_range_data['min']}-{stage_range_data['max']}"
        stage_range_avg = f"{stage_range_data['avgMin']}-{stage_range_data['avgMax']}"
        
        # Get recommendations for this dimension
        dimension_recommendations = []
        if 'recommendations' in scores:
            dimension_recommendations = [rec for rec in scores['recommendations'] if rec.get('category') == dimension_name]
        
        context = {
            'dimension_name': dimension_name,
            'score': f'{score:.1f}',
            'total_score': total_score,
            'stage': stage,
            'stage_range': self.get_stage_score_range(stage),
            'stage_range_points': stage_range_points,
            'stage_range_avg': stage_range_avg,
            'overview': dimension_data.get('summary', 'No overview available.'),
            'stage_meaning': stage_guidance.get('meaning', 'No stage meaning available.'),
            'core_message': stage_guidance.get('coreMessage', 'No core message available.'),
            'dimensions': json.dumps(dimensions),
            'client_scores': json.dumps(client_scores),
            'industry_benchmarks': json.dumps(industry_benchmarks),
            'current_dimension_index': dimension_index,
            'page_number': page_number,
            'total_pages': total_pages,
            'recommendations': dimension_recommendations
        }
        return render_to_string('pdf/dimension_page.html', context)

    def create_next_steps_page(self, total_pages):
        """Create next steps page using HTML template"""
        context = {
            'page_number': total_pages,
            'total_pages': total_pages
        }
        return render_to_string('pdf/next_steps.html', context)
    
    def create_combined_html(self, html_pages):
        """Combine HTML pages with proper print styling"""
        print_css = '''
        <style>
            @media print {
                @page {
                    size: A4 landscape;
                    margin: 0;
                }
                body {
                    margin: 0;
                    padding: 0;
                }
                .page {
                    page-break-after: always;
                    width: 1123px;
                    height: 794px;
                    display: flex;
                    flex-direction: column;
                }
                .page:last-child {
                    page-break-after: avoid;
                }
                .content {
                    display: flex !important;
                    flex-direction: row !important;
                    align-items: flex-start !important;
                }
                .chart-container {
                    width: 420px !important;
                    height: 420px !important;
                    flex-shrink: 0 !important;
                }
                .details-section {
                    flex: 1 !important;
                    margin-left: 40px !important;
                }
            }
            @media screen {
                body {
                    margin: 0;
                    padding: 20px;
                    background-color: #f5f5f5;
                }
                .page {
                    display: block;
                    width: 100%;
                    max-width: 1123px;
                    margin: 0 auto 30px auto;
                    background: white;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    border-radius: 8px;
                    overflow: hidden;
                }
            }
        </style>
        '''
        
        # Wrap each page
        pages_with_breaks = []
        for i, page in enumerate(html_pages):
            pages_with_breaks.append(f'<div class="page">{page}</div>')
        
        combined_html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>AI Maturity Assessment Report</title>
            {print_css}
        </head>
        <body>
            {''.join(pages_with_breaks)}
        </body>
        </html>
        '''
        
        return combined_html
    
    def html_to_pdf_browser(self, html_content, session_id):
        """Convert HTML to PDF using browser automation"""
        # Save HTML to temporary file
        html_filename = f'temp_report_{session_id}.html'
        pdf_filename = f'temp_report_{session_id}.pdf'
        
        try:
            # Write HTML file
            with open(html_filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            # Try different PDF conversion methods
            if platform.system() == 'Windows':
                # Try using Chrome/Edge for PDF conversion
                chrome_paths = [
                    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
                    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'
                ]
                
                for chrome_path in chrome_paths:
                    if os.path.exists(chrome_path):
                        cmd = [
                            chrome_path,
                            '--headless',
                            '--disable-gpu',
                            '--print-to-pdf=' + pdf_filename,
                            '--print-to-pdf-no-header',
                            '--no-margins',
                            html_filename
                        ]
                        
                        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                        if result.returncode == 0 and os.path.exists(pdf_filename):
                            # Read PDF file
                            with open(pdf_filename, 'rb') as f:
                                pdf_content = f.read()
                            
                            # Clean up temp files
                            os.remove(html_filename)
                            os.remove(pdf_filename)
                            
                            return BytesIO(pdf_content)
                        break
            
            # If browser conversion fails, clean up and raise exception
            if os.path.exists(html_filename):
                os.remove(html_filename)
            if os.path.exists(pdf_filename):
                os.remove(pdf_filename)
            
            raise Exception("Browser PDF conversion not available")
            
        except Exception as e:
            # Clean up temp files
            if os.path.exists(html_filename):
                os.remove(html_filename)
            if os.path.exists(pdf_filename):
                os.remove(pdf_filename)
            raise e

    def get_stage_from_score(self, score):
        """Get maturity stage from score"""
        if score < 2:
            return 'Nascent'
        elif score < 3:
            return 'Emerging'
        elif score < 4:
            return 'Scaling'
        elif score < 5:
            return 'Transforming'
        else:
            return 'Leading'

    def get_stage_guidance(self, dimension_name, stage):
        """Get stage-specific guidance for dimension - matches webapp radar.html exactly"""
        # Exact stage descriptions from webapp radar.html
        stage_descriptions = {
            'AI Vision & Strategic Alignment': {
                'Nascent': {
                    'meaning': 'At this stage, AI is almost invisible in the organization\'s strategy. It is absent from formal planning, and no documented vision or blueprint exists to guide its use. Leadership rarely references AI, and when it is mentioned, it carries little weight in decision-making. Any initiatives that do exist are isolated, experimental, and disconnected from business outcomes. Products and services show little to no sign of AI influence, leaving the company without a clear sense of direction for AI\'s role in its future. direction.',
                    'coreMessage': 'No AI vision, no alignment — progress depends on isolated experiments.'
                },
                'Emerging': {
                    'meaning': 'In the emerging stage, AI begins to appear in the strategic conversation, but only in a limited way. Some functions may draft informal visions or start exploring opportunities, yet there is no unified enterprise approach. Leadership still tends to view AI mainly as a tool for automation or efficiency rather than as a driver of transformation. Pilot projects surface across the business, but measurement is weak or nonexistent, making it difficult to tie them to outcomes. AI shows up experimentally in a handful of offerings, signaling curiosity but not yet commitment.',
                    'coreMessage': 'Draft vision exists but is siloed and inconsistently applied'
                },
                'Scaling': {
                    'meaning': 'When an organization reaches the scaling stage, AI becomes more explicitly woven into departmental or business-unit strategies. A documented AI vision or blueprint begins to take shape, and some functions are actively validating and adopting it. KPIs are tracked for a select set of high-priority initiatives, giving the company its first glimpse into measurable impact. Leadership increasingly positions AI as an important driver of change, though execution still varies across the enterprise. Some products and services visibly reflect the AI strategy, but adoption remains uneven and pockets of inconsistency persist. remain between businessunits.',
                    'coreMessage': 'AI is strategic, but delivery and alignment are uneven'
                },
                'Transforming': {
                    'meaning': 'Enterprise AI strategy is embedded into core business planning. Clear business impact metrics guide prioritization, and AI is viewed as a key lever for transformation across departments',
                    'coreMessage': 'AI is embedded in strategy and drives measurable impact across functions'
                },
                'Leading': {
                    'meaning': 'Organizations in the leading stage treat AI not just as part of their strategy, but as a defining element of their long-term positioning. The AI vision is fully institutionalized and guides priorities across every layer of the business. Every AI initiative is linked to measurable business impact, making accountability and value creation transparent. Leadership consistently frames AI as a core enabler of future business models, setting the tone for the entire organization. AI drives innovation pipelines and underpins how products and services are designed, built, and delivered. Companies at this stage are not only advanced internally — they also set benchmarks for their industry, shaping how AI transformation is understood and pursued by others.',
                    'coreMessage': 'AI vision defines business future — fully embedded, measurable, and transformative'
                }
            },
            'Leadership & Governance': {
                'Nascent': {
                    'meaning': 'At the nascent stage, leadership has no unified stance on AI, and any interest that exists is fragmented across individuals. No one in the organization is formally accountable for AI, leaving initiatives to emerge sporadically from isolated teams. Business and technology leaders operate in silos, and decisions about AI are taken ad hoc, often without transparency or consistency. No executive forum or steering committee exists to provide oversight, meaning AI initiatives lack visibility at the top and remain disconnected from enterprise strategy.',
                    'coreMessage': 'AI leadership is absent, and initiatives lack direction or oversight.'
                },
                'Emerging': {
                    'meaning': 'In the emerging stage, leadership begins to experiment with AI, often driven by one or two senior leaders who recognize its potential but without a shared vision. Ownership remains fragmented, typically spread across IT or business units, with no clear mandate or authority. Collaboration between business and technology leaders occurs occasionally but only in the context of specific projects, not as a systematic practice. Governance starts to appear in the form of loose guidelines, though they are inconsistently applied. Discussions about AI may surface during budget cycles, but oversight is sporadic and not formalized into structured forums.',
                    'coreMessage': 'AI leadership interest exists, but ownership and governance remain fragmented.'
                },
                'Scaling': {
                    'meaning': 'At the scaling stage, leadership moves from experimentation to structured oversight. Executive sponsors not only champion AI but also begin to allocate meaningful budgets aligned with business goals. Governance processes are formalized, with cadence meetings, approval workflows, and accountability mechanisms in place. AI projects are prioritized through a portfolio lens, ensuring alignment with both value potential and risk management. Leaders demand measurable outcomes, linking initiatives to key performance indicators. While execution is improving, the challenge lies in ensuring that governance keeps pace with the growing volume and complexity of AI projects.',
                    'coreMessage': 'AI leadership structures are forming, but authority and influence are still limited.'
                },
                'Transforming': {
                    'meaning': 'In the transforming stage, leadership fully integrates AI into strategic planning and enterprise governance. AI is no longer treated as an add-on but as a critical enabler of transformation, with sponsorship anchored at the C-suite level and often championed directly by the CEO. Decision-making becomes evidence-driven, supported by dashboards and performance reviews that track AI\'s contribution to outcomes such as growth, efficiency, and risk reduction. Governance frameworks are mature, balancing innovation with compliance, ethics, and security. Leaders foster cross-functional collaboration, ensuring that accountability for AI outcomes extends beyond IT or data teams and becomes a shared responsibility across the business.',
                    'coreMessage': 'AI is championed at the top, with formal governance and shared accountability across the business.'
                },
                'Leading': {
                    'meaning': 'At the leading stage, AI governance becomes a hallmark of organizational leadership excellence. The board and C-suite treat AI as a core driver of competitive advantage and ensure that governance is adaptive, transparent, and forward-looking. Leadership not only provides strong sponsorship but also sets clear ethical guardrails and risk frameworks, influencing industry norms and sometimes shaping regulatory conversations. Governance structures evolve into an operating rhythm that enables agility without sacrificing accountability. Leaders act as role models, linking AI-driven transformation directly to the company\'s purpose, culture, and stakeholder trust. At this level, leadership and governance shift from enabling adoption to sustaining an AI-first organization.',
                    'coreMessage': 'AI leadership is institutionalized, with board-level oversight and governance as a competitive advantage.'
                }
            },
            'Use Case Portfolio & Prioritization': {
                'Nascent': {
                    'meaning': 'At this stage, AI use cases are nonexistent or limited to isolated, exploratory pilots. There is no formal prioritization framework, and initiatives are chosen based on enthusiasm or ad hoc needs rather than strategic alignment. Metrics and KPIs are absent, meaning there is no way to measure outcomes or value. Pilots rarely, if ever, progress into production. No playbooks or reusable templates exist, so even learnings from early experiments are not institutionalized.',
                    'coreMessage': 'AI adoption is absent or scattered — no prioritization, no measurement, no scale.'
                },
                'Emerging': {
                    'meaning': 'AI pilots start to appear in select business units, often driven by individual leaders or technology teams. Some level of prioritization emerges, usually based on urgency or ROI, but it lacks consistency and strategic direction. Basic output metrics (like model accuracy) may be tracked, but these are not connected to business outcomes. A handful of pilots progress to limited use, but most stall at proof-of-concept. Teams may experiment with templates or reusable assets, but they are fragmented and inconsistent.',
                    'coreMessage': 'Pilots exist, but prioritization and metrics are inconsistent — adoption remains experimental.'
                },
                'Scaling': {
                    'meaning': 'Organizations begin to formalize how use cases are selected, often evaluating them against business value, feasibility, and risk. High-priority pilots are linked to defined success metrics, and more projects progress into production. While success is uneven, some clear wins demonstrate tangible value. Playbooks or templates start to emerge for repeatable use cases, though they are not universally applied. The organization is learning how to scale, but adoption remains uneven across departments.',
                    'coreMessage': 'Prioritization is structured and pilots are scaling, though inconsistently.'
                },
                'Transforming': {
                    'meaning': 'Use case portfolio management becomes systematic and enterprise-wide. A standardized prioritization model is consistently applied, ensuring that AI investments align with business strategy and risk appetite. The majority of AI initiatives are linked to measurable KPIs, and pilots regularly transition into production with proven impact. Playbooks and reusable assets are widely used, accelerating time-to-value. AI is no longer experimental — it is embedded into workflows and decision-making across functions.',
                    'coreMessage': 'AI portfolio is strategically prioritized, KPI-driven, and delivering measurable business value.'
                },
                'Leading': {
                    'meaning': 'At the leading stage, AI use case portfolio management is industrialized and continuously refreshed. Every initiative is prioritized against a unified, enterprise-wide framework that balances value, feasibility, and risk. KPIs are embedded into all initiatives, and pilots have a consistently high conversion rate into scalable, production-ready systems. A robust library of playbooks, templates, and accelerators institutionalizes best practices, making adoption repeatable and fast. The organization not only executes effectively but also shapes industry benchmarks, using its AI portfolio as a competitive differentiator.',
                    'coreMessage': 'AI portfolio is industrialized — repeatable, scalable, and transformative at enterprise scale.'
                }
            },
            'Data Infrastructure & Quality': {
                'Nascent': {
                    'meaning': 'Data is fragmented, siloed, and often unreliable. Teams struggle to locate or access usable data, and no catalog or inventory exists. Quality is not validated, and legacy systems hinder AI workloads. Integration between sources is nonexistent, meaning AI initiatives are blocked at the starting line.',
                    'coreMessage': 'Fragmented, inaccessible, low-quality data blocks AI progress.'
                },
                'Emerging': {
                    'meaning': 'Basic efforts begin to address data foundations. A pilot catalog or limited inventories may exist, but they are isolated to certain domains. Ad hoc integrations are built when needed, but they are fragile and inconsistent. Data warehouses or basic cleaning is underway, but scalability remains limited. Quality validation starts for select datasets, though confidence across teams remains low. AI can move past pure experimentation, but foundations are still shaky.',
                    'coreMessage': 'Early data foundations exist, but integration and quality are inconsistent.'
                },
                'Scaling': {
                    'meaning': 'Data accessibility improves through unified platforms that make curated data available across multiple functions. A searchable catalog exists for much of the enterprise, improving visibility. Systematic pipelines begin to integrate internal and external data sources, creating broader coverage. Infrastructure is reliable enough to support key AI projects, and governance frameworks for data begin to formalize. Quality checks are applied at scale, though not yet fully automated.',
                    'coreMessage': 'Integrated data platforms and governance support expanding AI use.'
                },
                'Transforming': {
                    'meaning': 'Data is treated as a managed enterprise asset. Real-time, governed, and on-demand access is available to most teams, and a dynamic catalog ensures discoverability and usability. Integration pipelines unify data across the business, and infrastructure is enterprise-grade with elasticity to support large-scale AI workloads. Quality checks and lineage are embedded into processes, ensuring trust in AI outputs. Teams can experiment, scale, and deploy AI quickly without being slowed by data issues.',
                    'coreMessage': 'Enterprise-ready, governed data foundation powers transformation.'
                },
                'Leading': {
                    'meaning': 'At this stage, the organization achieves a fully industrialized, intelligent data ecosystem. Data is proactively managed, continuously updated, and instantly available enterprise-wide. Catalogs are dynamic and AI-assisted, guiding discoverability and compliance in real time. Integration is seamless, spanning multi-cloud and external ecosystems. Infrastructure is AI-first — cloud-native, automated, and self-optimizing — designed to power advanced AI (e.g., generative AI, real-time personalization) at scale. Data quality is continuously monitored and improved, ensuring trust across every AI initiative.',
                    'coreMessage': 'Intelligent, AI-first data ecosystem drives enterprise-wide scale and industry leadership.'
                }
            },
            'Talent & Culture': {
                'Nascent': {
                    'meaning': 'The organization has no meaningful AI/ML expertise in-house, and business teams lack awareness or training. Collaboration between business and technical teams is minimal or nonexistent, with work handled in silos. There is no defined operating model for AI, and roles are unclear. The culture is risk-averse, discouraging experimentation or innovation. AI remains theoretical with no organizational readiness to support it.',
                    'coreMessage': 'No AI talent, no skills, no culture — readiness is near zero.'
                },
                'Emerging': {
                    'meaning': 'Early steps are taken to introduce AI talent and cultural awareness. One or two specialists or analysts may exist, and sporadic awareness sessions help expose business teams to AI concepts. Collaboration happens occasionally but is transactional rather than strategic. Role clarity is weak, with AI work often assigned ad hoc. Cultural openness to AI is limited, with experimentation happening only in isolated pockets. AI projects exist, but people and processes are not yet aligned.',
                    'coreMessage': 'Initial AI skills and awareness exist, but adoption is fragmented and cultural buy-in is weak.'
                },
                'Scaling': {
                    'meaning': 'Dedicated AI/ML teams begin to form, supporting a growing number of use cases across the business. Select teams are being upskilled with use-case-specific training, and collaboration between business and technical groups improves through joint planning. Role clarity is emerging, with defined responsibilities in some departments. Cultural openness to experimentation is growing, with some teams encouraged to test AI ideas. The foundation for AI readiness is visible but inconsistent across the enterprise.',
                    'coreMessage': 'AI skills and collaboration are growing, but maturity is uneven across the organization.'
                },
                'Transforming': {
                    'meaning': 'Cross-functional AI/ML specialists are embedded across departments, enabling broad collaboration. Business teams benefit from ongoing learning programs, and AI literacy is becoming part of the organizational fabric. Operating models are formalized, with clear roles and responsibilities across product, data, and technical teams. A culture of experimentation is promoted, especially in innovation units, allowing safe-to-fail pilots. AI readiness is no longer a bottleneck — people, skills, and structures enable transformation.',
                    'coreMessage': 'Skilled teams, structured roles, and cultural readiness drive enterprise AI transformation.'
                },
                'Leading': {
                    'meaning': 'AI talent and skills are deeply institutionalized across both business and technical units. Continuous, enterprise-wide AI literacy programs empower all employees to use and co-create AI solutions. Collaboration is seamless, with cross-functional teams co-owning and scaling AI initiatives. Operating models are enterprise-wide, clearly defining accountability, delivery, and governance for AI. The culture rewards a growth mindset and test-and-learn approaches, making experimentation and adaptation a core strength. The organization is not just AI-ready — it sets benchmarks for talent and cultural alignment in its industry.',
                    'coreMessage': 'AI talent, skills, and culture are institutionalized — enabling sustained, enterprise-wide innovation.'
                }
            },
            'Responsible AI & Risk': {
                'Nascent': {
                    'meaning': 'The organization has no formal Responsible AI policies or frameworks in place. AI models are deployed without checks for bias, fairness, or unintended consequences, and no oversight processes exist. There is no accountability when AI-driven decisions impact users or stakeholders. Risks such as drift, misuse, or compliance failures are only recognized after issues arise. At this stage, AI may be used, but it operates without safeguards, exposing the organization to ethical, reputational, and regulatory risks.',
                    'coreMessage': 'No guardrails — AI is unmanaged, unaccountable, and high-risk.'
                },
                'Emerging': {
                    'meaning': 'Early conversations about Responsible AI begin, but practices remain inconsistent. Draft guidelines may be in progress, and basic fairness checks are applied in limited projects. Oversight is informal, with deployment decisions left to individual project teams or leaders. Accountability for AI decisions is reactive, usually addressed only when problems surface. Risk management practices are ad hoc, and monitoring is limited to isolated pilots. The intent to act responsibly exists, but it has not yet been institutionalized.',
                    'coreMessage': 'Awareness is growing, but Responsible AI is patchy and reactive.'
                },
                'Scaling': {
                    'meaning': 'Responsible AI starts to take shape through formalized but uneven practices. A policy framework may be approved, and fairness testing occurs in select high-risk projects. Oversight exists for critical models, often through designated leaders or committees. Accountability mechanisms for AI decisions are clearer, though not yet enterprise-wide. Some projects include risk assessments and mitigation plans, supported by partial monitoring tools. Responsible AI practices are gaining traction but lack full coverage.',
                    'coreMessage': 'Policies and controls are emerging, but not consistently applied across AI.'
                },
                'Transforming': {
                    'meaning': 'Responsible AI becomes a structured part of governance. Policies and ethical principles are codified, embedded into workflows, and communicated enterprise-wide. Bias, fairness, and unintended consequence testing are applied across most initiatives. Oversight is cross-functional, with governance processes for high-impact and regulated models. Accountability is built into governance structures, with clear escalation paths when AI impacts users. Risk monitoring tools track performance, drift, and compliance systematically. Responsible AI moves from theory to practice, reducing organizational exposure.',
                    'coreMessage': 'Responsible AI is structured, governed, and embedded into delivery.'
                },
                'Leading': {
                    'meaning': 'Responsible AI is institutionalized and sets benchmarks for the industry. Policies are deeply embedded into design, development, and deployment, with automation supporting fairness, bias, and risk testing across the lifecycle. Formal governance boards oversee all models, with clear accountability at every level. AI-driven decisions are proactively explained, transparent, and aligned with user trust and ethical standards. Model risk management is enterprise-wide, proactive, and compliance-aligned, ensuring early detection and mitigation of drift, misuse, or performance failures. The organization demonstrates leadership in ethical AI, often shaping industry norms and regulatory best practices.',
                    'coreMessage': 'Responsible AI is proactive, standardized, and sets the benchmark for trust and safety.'
                }
            },
            'Measurement, Scaling & ROI': {
                'Nascent': {
                    'meaning': 'At this stage, AI initiatives are launched without any formal measurement of impact. ROI is not tracked, and there is no clear link between AI and business outcomes such as cost savings, growth, or CX. No dashboards exist, making adoption and performance invisible to leadership. Failures are ignored, with no effort to extract lessons. Successful pilots, if any, are not scaled beyond isolated experiments. AI efforts remain tactical and disconnected from enterprise value.',
                    'coreMessage': 'No measurement, no learning, no scale.'
                },
                'Emerging': {
                    'meaning': 'Early attempts are made to measure AI impact, but practices are inconsistent. Success is often gauged qualitatively or through anecdotal wins. ROI is sometimes estimated after pilots, but not standardized. Tracking is manual, handled within teams, and limited to isolated models. Failures may trigger informal reflections, but insights rarely shape future efforts. A few pilots are converted into internal guides, but no formal scaling approach exists. AI projects begin to show promise but remain opportunistic.',
                    'coreMessage': 'Early signs of impact, but measurement and scaling are fragmented.'
                },
                'Scaling': {
                    'meaning': 'AI initiatives increasingly link to measurable outcomes, with some use cases reporting ROI aligned to KPIs. Dashboards exist for critical models or departments, giving partial visibility into performance and adoption. Post-mortems are held for select pilots, and insights are documented more systematically. Some scaling playbooks emerge, helping replicate successful projects, though adoption is uneven across the enterprise. At this stage, AI value is visible, but governance and measurement are not yet universal.',
                    'coreMessage': 'ROI and outcomes are visible, but scaling and governance are inconsistent.'
                },
                'Transforming': {
                    'meaning': 'ROI measurement is standardized and embedded into most AI initiatives, tied directly to business KPIs. Nearly all projects report against strategic outcomes like growth, cost, CX, or sustainability. Dashboards track performance and adoption across functions, enabling leadership oversight. Lessons from failed initiatives are documented, shared, and actively used to shape future project design and governance. Scaling is systematic, supported by playbooks and SOPs that accelerate reuse and rollout. AI becomes a managed portfolio of initiatives with proven business value.',
                    'coreMessage': 'AI value is measurable, repeatable, and informs enterprise-wide scaling.'
                },
                'Leading': {
                    'meaning': 'At the leading stage, AI impact measurement is institutionalized across the organization. Every initiative is mapped to one or more strategic vectors and tracked through a standardized ROI framework. Executive-level scorecards provide real-time visibility into adoption, maturity, and value creation. Failures are not just reviewed — they systematically feed back into governance and design, making AI efforts continuously self-improving. Scaling is enterprise-wide, supported by a robust framework that ensures reuse, rollout, and integration across functions. AI investment decisions are evidence-driven, maximizing both business value and innovation.',
                    'coreMessage': 'AI is industrialized — measurable, scalable, and continuously improving.'
                }
            },
            'AI Operating Model & Change Readiness': {
                'Nascent': {
                    'meaning': 'At this stage, the organization has no defined AI operating model. Roles and responsibilities are scattered, and there is no structured approach to delivering value from AI. Change management is absent, with little to no communication around adoption. Business units have no incentives to adopt AI, and there are no champions or advocates promoting its use. Experimentation is minimal or non-existent, with no sandboxes or safe environments for teams to try AI tools. AI efforts remain ad hoc, fragmented, and disconnected from enterprise priorities.',
                    'coreMessage': 'No structure, no incentives, no readiness for AI adoption.'
                },
                'Emerging': {
                    'meaning': 'Early steps toward AI adoption begin, but structures remain weak. A central AI or analytics team may exist, but it operates in isolation from the business. Communication around AI adoption is reactive, often triggered only when challenges arise. A few employees act as informal AI ambassadors, but their influence is limited. Some teams may experiment with AI in controlled or technical settings, though access is restricted. Business incentives for adoption are vague or non-existent. Momentum is building, but it is not coordinated or supported enterprise-wide.',
                    'coreMessage': 'Initial structures and advocates exist, but adoption is fragmented and reactive.'
                },
                'Scaling': {
                    'meaning': 'A federated operating model begins to emerge, with shared responsibilities between central and business teams. Change management practices improve, with some trainings and awareness programs offered post-rollout. Incentives for adoption start to take shape, such as budget relief or productivity credits for business units using AI. Formal AI champions are named in select functions, helping build awareness and momentum. Sandboxes exist in some departments, allowing limited experimentation. AI adoption is growing, but consistency and alignment across the enterprise remain uneven.',
                    'coreMessage': 'Shared models, incentives, and experimentation exist, but maturity is uneven.'
                },
                'Transforming': {
                    'meaning': 'An enterprise operating model is in place, aligning ownership, delivery, and value across functions. Change management is embedded into most AI programs, with proactive communication and enablement. AI adoption is tied to OKRs or KPIs, ensuring business accountability. Champions and change agents are designated across departments, driving awareness and cross-functional collaboration. Open-access sandboxes are available to business teams, promoting innovation and safe experimentation. AI adoption is no longer optional — it is becoming systematic and structured.',
                    'coreMessage': 'AI adoption is structured, incentivized, and supported by culture and tools.'
                },
                'Leading': {
                    'meaning': 'The organization operates with a fully institutionalized AI operating model, integrating ownership, delivery, and governance across the enterprise. Change management is proactive and built into every AI initiative, ensuring smooth adoption from planning to execution. AI adoption is directly tied to performance metrics and business outcomes, incentivizing scale. A cross-functional enablement team drives enterprise-wide awareness, training, and adoption. Sandboxes are enterprise-funded, governed, and embedded into innovation programs, enabling both technical and business teams to experiment safely. AI adoption is sustained, scalable, and culturally ingrained.',
                    'coreMessage': 'AI operating model and change readiness are institutionalized — enabling sustainable, enterprise-wide adoption.'
                }
            },
            'Technology & AI Infrastructure': {
                'Nascent': {
                    'meaning': 'The organization lacks AI-ready infrastructure. There are no dedicated environments for model training or deployment, and any AI work depends on ad hoc setups. There are no operational tools, no version control, and no monitoring in place. Real-time or streaming capabilities are absent. AI development is experimental, fragile, and unsustainable at scale.',
                    'coreMessage': 'No infrastructure — AI is experimental and unsustainable.'
                },
                'Emerging': {
                    'meaning': 'Early infrastructure for AI experimentation begins to appear, such as limited cloud instances or testing environments. Scripts and workflows are managed manually, with little automation. Basic documentation exists for select models, but versioning is inconsistent. Some pipelines support near-real-time use, but they are not scalable. Monitoring is manual and sporadic, providing minimal visibility into model performance. AI efforts are possible but remain fragile and inconsistent.',
                    'coreMessage': 'Early foundations exist, but practices are ad hoc and fragile.'
                },
                'Scaling': {
                    'meaning': 'Dedicated servers, cloud instances, and versioning tools support AI initiatives more systematically. MLOps tools are piloted or adopted in parts of the organization, enabling repeatable workflows. Some models are version-controlled, reproducible, and auditable. Limited real-time AI use cases exist in testing or early production. Monitoring dashboards track performance and drift for critical models, though not enterprise-wide. AI infrastructure supports scaling, but practices remain uneven.',
                    'coreMessage': 'Infrastructure and tools support scaling, but adoption is inconsistent.'
                },
                'Transforming': {
                    'meaning': 'Infrastructure becomes enterprise-grade, supporting large-scale AI training, deployment, and real-time use cases. MLOps and AIOps platforms are established across departments, automating much of the lifecycle. All models are tracked and reproducible, with audit trails and rollback options. Real-time inference powers multiple business functions, while monitoring systems detect performance changes and drift with partial automation. The stack is reliable, scalable, and capable of driving enterprise-wide AI adoption.',
                    'coreMessage': 'Enterprise-grade infrastructure operationalizes AI at scale.'
                },
                'Leading': {
                    'meaning': 'The organization operates with a fully optimized, AI-first technology environment. Infrastructure supports GenAI, multi-model orchestration, and real-time streaming as a default. MLOps pipelines fully automate training, deployment, monitoring, and retraining across the lifecycle. Every model has complete lineage, version history, and rollback capabilities. Real-time inference is standard, powering advanced use cases across industries. Monitoring and drift management are proactive, with automated retraining pipelines. The stack is not just scalable — it is adaptive, intelligent, and benchmark-setting.',
                    'coreMessage': 'AI infrastructure is enterprise-optimized, automated, and industry-leading.'
                }
            }
        }
        
        # Get dimension-specific guidance or fall back to generic
        dimension_guidance = stage_descriptions.get(dimension_name, {})
        stage_guidance = dimension_guidance.get(stage, {})
        
        if not stage_guidance:
            # Generic fallback
            generic_guidance = {
                'Nascent': {
                    'meaning': 'Initial awareness and foundational understanding of AI potential.',
                    'coreMessage': 'Focus on building awareness and identifying initial opportunities.'
                },
                'Emerging': {
                    'meaning': 'AI initiatives increasingly link to measurable outcomes, with some use cases reporting ROI aligned to KPIs. Dashboards exist for critical models or departments, giving partial visibility into performance and adoption. Post-mortems are held for select pilots, and insights are documented more systematically. Some scaling playbooks emerge, helping replicate successful projects, though adoption is uneven across the enterprise. At this stage, AI value is visible, but governance and measurement are not yet universal.',
                    'coreMessage': 'ROI and outcomes are visible, but scaling and governance are inconsistent.'
                },
                'Scaling': {
                    'meaning': 'Systematic adoption with multiple successful implementations.',
                    'coreMessage': 'Focus on scaling successful pilots and building repeatable processes.'
                },
                'Transforming': {
                    'meaning': 'Strategic integration with measurable business impact.',
                    'coreMessage': 'Optimize existing capabilities and drive enterprise-wide adoption.'
                },
                'Leading': {
                    'meaning': 'Industry benchmark with continuous innovation and optimization.',
                    'coreMessage': 'Maintain competitive advantage and drive industry standards.'
                }
            }
            stage_guidance = generic_guidance.get(stage, {})
        
        return stage_guidance

    def get_stage_score_range(self, stage):
        """Get score range for a maturity stage - matches webapp scoring"""
        scoring_mechanism = {
            'Nascent': {'min': 5, 'max': 9, 'avgMin': 1.0, 'avgMax': 1.9},
            'Emerging': {'min': 10, 'max': 12, 'avgMin': 2.0, 'avgMax': 2.4},
            'Scaling': {'min': 13, 'max': 17, 'avgMin': 2.5, 'avgMax': 3.4},
            'Transforming': {'min': 18, 'max': 21, 'avgMin': 3.5, 'avgMax': 4.2},
            'Leading': {'min': 22, 'max': 25, 'avgMin': 4.3, 'avgMax': 5.0}
        }
        stage_data = scoring_mechanism.get(stage, scoring_mechanism['Nascent'])
        return f"{stage_data['avgMin']}-{stage_data['avgMax']} average score"
    
    def generate_html_report(self, scores, dimensions_data, session_id, company_name):
        """Generate HTML report content using proper templates"""
        try:
            # Get real assessment data
            from .models import AssessmentResponse
            assessment = AssessmentResponse()
            actual_scores = assessment.calculate_scores(session_id)
            
            # Use actual category scores from assessment
            dimensions = list(actual_scores['category_scores'].keys())
            client_scores = list(actual_scores['category_scores'].values())
            industry_benchmarks = [2.8, 2.5, 2.7, 2.6, 2.9, 2.4, 2.2, 2.5, 2.3][:len(dimensions)]
            
            total_pages = 3 + len(dimensions)  # Cover + Radar + Dimensions + Next Steps
            
            # Generate HTML pages using templates
            html_pages = []
            
            # Cover page
            cover_html = self.create_cover_page(company_name)
            html_pages.append(cover_html)
            
            # Radar overview page
            radar_html = self.create_radar_overview_page(dimensions, client_scores, industry_benchmarks, total_pages, actual_scores)
            html_pages.append(radar_html)
            
            # Dimension pages - use proper templates with radar on left, content on right
            for i, dimension in enumerate(dimensions):
                dimension_html = self.create_dimension_page(
                    dimension, dimensions_data.get(dimension, {}), actual_scores, dimensions, client_scores, 
                    industry_benchmarks, i, i+3, total_pages
                )
                html_pages.append(dimension_html)
            
            # Next steps page
            next_steps_html = self.create_next_steps_page(total_pages)
            html_pages.append(next_steps_html)
            
            # Combine all HTML pages with proper page breaks
            combined_html = self.create_combined_html(html_pages)
            
            return combined_html
            
        except Exception as e:
            print(f"Error generating HTML report: {str(e)}")
            return f"<html><body><h1>Error generating report: {str(e)}</h1></body></html>"