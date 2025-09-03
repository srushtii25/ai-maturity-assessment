# # Complete Assessment questions for all 12 categories
# ASSESSMENT_QUESTIONS = {
#     'AI Vision & Strategy': [
#         'Which statement best describes your AI vision and North Star?',
#         'Which statement best describes how AI is integrated into your enterprise strategy?',
#         'Which statement best describes your AI KPIs and success metrics?',
#         'Which statement best describes your AI roadmap and planning?',
#         'Which statement best describes how your AI strategy is communicated?'
#     ],
#     'Leadership & Governance': [
#         'Which statement best describes executive sponsorship for AI?',
#         'Which statement best describes your AI governance charter and decision rights?',
#         'Which statement best describes your AI budget and funding commitment?',
#         'Which statement best describes your AI project approval and oversight process?',
#         'Which statement best describes how you track AI benefits and outcomes?'
#     ],
#     'Operating Model & Funding': [
#         'Which statement best describes your AI operating model and organizational structure?',
#         'Which statement best describes your AI funding model and resource allocation?',
#         'Which statement best describes how you manage AI talent and capabilities?',
#         'Which statement best describes your AI delivery processes and methodologies?',
#         'Which statement best describes how you scale AI initiatives across the organization?'
#     ],
#     'Data Foundations & Quality': [
#         'Which statement best describes your data accessibility and usability for AI?',
#         'Which statement best describes your data quality and reliability?',
#         'Which statement best describes your data integration and connectivity?',
#         'Which statement best describes your data infrastructure scalability for AI workloads?',
#         'Which statement best describes your data preparation and preprocessing capabilities?'
#     ],
#     'Data Governance & Security': [
#         'Which statement best describes your data governance framework?',
#         'Which statement best describes your data security and privacy controls?',
#         'Which statement best describes your data access management and permissions?',
#         'Which statement best describes your data lineage and audit capabilities?',
#         'Which statement best describes your data compliance and regulatory adherence?'
#     ],
#     'Platform & Integration Architecture': [
#         'Which statement best describes your AI/ML platform and infrastructure maturity?',
#         'Which statement best describes your AI system integration with existing applications?',
#         'Which statement best describes your AI architecture scalability and flexibility?',
#         'Which statement best describes your API and integration capabilities?',
#         'Which statement best describes your AI model deployment and serving capabilities?'
#     ],
#     'ML Lifecycle & Model Ops': [
#         'Which statement best describes your ML development and experimentation processes?',
#         'Which statement best describes your model training and validation approach?',
#         'Which statement best describes your model deployment and release processes?',
#         'Which statement best describes your model monitoring and maintenance in production?',
#         'Which statement best describes your model versioning and lifecycle management?'
#     ],
#     'Portfolio & Value': [
#         'Which statement best describes your AI project intake and prioritization?',
#         'Which statement best describes your AI business cases and value models?',
#         'Which statement best describes how you track and measure realized AI value?',
#         'Which statement best describes your AI portfolio governance and decision-making?',
#         'Which statement best describes your AI portfolio review process and cadence?'
#     ],
#     'Talent & Culture': [
#         'Which statement best describes your AI talent pool and capabilities?',
#         'Which statement best describes your AI training and development programs?',
#         'Which statement best describes your AI culture and mindset across the organization?',
#         'Which statement best describes how you attract and retain AI talent?',
#         'Which statement best describes your AI knowledge sharing and collaboration?'
#     ],
#     'Responsible AI & Risk': [
#         'Which statement best describes your responsible AI framework and principles?',
#         'Which statement best describes your AI risk assessment and mitigation processes?',
#         'Which statement best describes your AI fairness, transparency, and explainability?',
#         'Which statement best describes your AI ethics and bias monitoring capabilities?',
#         'Which statement best describes your AI regulatory and compliance management?'
#     ],
#     'Change Management & Adoption': [
#         'Which statement best describes your change strategy and stakeholder engagement?',
#         'Which statement best describes your communication approach and messaging?',
#         'Which statement best describes your training and enablement programs?',
#         'Which statement best describes change champions and local support?',
#         'Which statement best describes how you measure adoption and act on feedback?'
#     ],
#     'Customer Partner Ecosystem': [
#         'Which statement best describes how you capture and validate customer demand for AI offerings?',
#         'Which statement best describes your partner strategy and selection/due diligence?',
#         'Which statement best describes your commercial/legal frameworks (MSA/SOW, DPA, IP/indemnity)?',
#         'Which statement best describes joint delivery and enablement with customers/partners?',
#         'Which statement best describes performance management (SLAs/QBRs), risk, and exit/renewal?'
#     ]
# }

# # Answer options for each question (A=1, B=2, C=3, D=4, E=5)
# ANSWER_OPTIONS = {
#     'AI Vision & Strategy': {
#         'Q1': {
#             'A': 'We do not have a documented AI vision or North Star.',
#             'B': 'AI vision exists informally; direction is unclear.',
#             'C': 'A draft AI vision exists for priority areas.',
#             'D': 'AI vision is documented and tied to business outcomes.',
#             'E': 'AI North Star is enterprise-wide, OKR-linked, and cascaded into BU roadmaps.'
#         },
#         'Q2': {
#             'A': 'AI is not mentioned in enterprise strategy.',
#             'B': 'AI appears in strategy documents but lacks specifics.',
#             'C': 'AI is included in strategy with basic priorities.',
#             'D': 'AI strategy is integrated with clear themes and owners.',
#             'E': 'AI is core to enterprise strategy with quarterly reviews and BU alignment.'
#         },
#         'Q3': {
#             'A': 'We do not track AI-specific KPIs.',
#             'B': 'AI metrics exist but are inconsistent or unreliable.',
#             'C': 'Basic AI KPIs exist for priority initiatives.',
#             'D': 'Most AI initiatives have defined KPIs and success metrics.',
#             'E': 'Enterprise AI KPIs are tied to business outcomes with regular reporting.'
#         },
#         'Q4': {
#             'A': 'We do not have an AI roadmap.',
#             'B': 'AI roadmap exists but is high-level or outdated.',
#             'C': 'Roadmap exists for priority AI initiatives.',
#             'D': 'AI roadmap is capacity-aligned with quarterly updates.',
#             'E': 'Enterprise AI roadmap with scenarios, risks, and dependencies is actively managed.'
#         },
#         'Q5': {
#             'A': 'AI strategy is not communicated beyond leadership.',
#             'B': 'AI strategy is shared informally or inconsistently.',
#             'C': 'AI strategy is communicated to key stakeholders.',
#             'D': 'AI strategy is regularly communicated with narrative packs and FAQs.',
#             'E': 'AI strategy is part of enterprise communications with quarterly all-hands and updates.'
#         }
#     },
#     'Change Management & Adoption': {
#         'Q1': {
#             'A': 'We do not run structured change management.',
#             'B': 'Change happens informally; stakeholders are unclear.',
#             'C': 'Basic change plans exist for priority initiatives.',
#             'D': 'Most changes have stakeholder maps and engagement plans.',
#             'E': 'Enterprise change strategy with impact analysis and success metrics drives all initiatives.'
#         },
#         'Q2': {
#             'A': 'We do not have consistent messaging or communication.',
#             'B': 'Messages are ad hoc; narrative is unclear.',
#             'C': 'Core messages exist for priority changes.',
#             'D': 'Most changes have narrative packs and communication calendars.',
#             'E': 'Enterprise narrative with consistent messaging and multi-channel campaigns drives adoption.'
#         },
#         'Q3': {
#             'A': 'We do not provide training or enablement.',
#             'B': 'Training is informal; materials are inconsistent.',
#             'C': 'Basic training and job aids exist for priority changes.',
#             'D': 'Most changes ship with role-based training, guided tours, and playbooks.',
#             'E': 'Training is continuous with in-product guidance, credentialing, and refreshers based on feedback.'
#         },
#         'Q4': {
#             'A': 'We do not have change champions or local support.',
#             'B': 'A few volunteers help informally.',
#             'C': 'Named champions exist for priority areas with light coordination.',
#             'D': 'A champion network operates with enablement kits and office hours.',
#             'E': 'An enterprise network with incentives, KPIs, and feedback loops drives adoption.'
#         },
#         'Q5': {
#             'A': 'We do not measure adoption or collect feedback.',
#             'B': 'Anecdotal feedback is collected; metrics are unreliable.',
#             'C': 'Basic usage/adoption metrics exist for priority changes.',
#             'D': 'Most changes have dashboards and action trackers for feedback.',
#             'E': 'Enterprise adoption KPIs, surveys, and behavioral metrics drive re-plans and rollbacks.'
#         }
#     },
#     'Customer Partner Ecosystem': {
#         'Q1': {
#             'A': 'We do not run structured customer discovery or validation.',
#             'B': 'We collect ad hoc feedback; signals are anecdotal.',
#             'C': 'We run interviews/surveys for priority offers; findings are documented.',
#             'D': 'We use a repeatable discovery process with win/loss and pilot metrics.',
#             'E': 'We operate ongoing discovery with segment analytics and pipeline-to-adoption conversion targets.'
#         },
#         'Q2': {
#             'A': 'We do not have a defined partner strategy for AI.',
#             'B': 'We add partners opportunistically; criteria are unclear.',
#             'C': 'We apply basic selection criteria and reference checks for key partners.',
#             'D': 'We run structured due diligence (capability, security, financials) with tiering.',
#             'E': 'We manage a portfolio strategy with tiered partners, diversification, and renewal/exit rules.'
#         },
#         'Q3': {
#             'A': 'We do not have standard contracts or compliance terms for AI work.',
#             'B': 'We reuse generic terms; AI/IP/privacy issues are not explicit.',
#             'C': 'Standard MSAs/DPAs exist for priority engagements.',
#             'D': 'Contracts cover AI-specific IP, data rights, security, and SLAs with approvals.',
#             'E': 'Enterprise templates are versioned with playbooks; exceptions and approvals are auditable.'
#         },
#         'Q4': {
#             'A': 'We do not run structured co-delivery or enablement.',
#             'B': 'Some joint work happens; roles and readiness are unclear.',
#             'C': 'Playbooks exist for pilots and integrations on priority accounts.',
#             'D': 'Most deals run with co-sell kits, integration templates, and support readiness.',
#             'E': 'Enterprise co-delivery with repeatable blueprints, certifications, and shared success plans.'
#         },
#         'Q5': {
#             'A': 'We do not track partner/customer performance or risk.',
#             'B': 'We review performance informally; SLAs are rare.',
#             'C': 'SLAs and quarterly reviews exist for priority relationships.',
#             'D': 'Most relationships have KPIs, QBRs, and risk registers with actions.',
#             'E': 'Enterprise scorecards, health/risk dashboards, and exit/renewal playbooks are enforced.'
#         }
#     }
# }

# # Category rules with conditions and nudges
# CATEGORY_RULES = {
#     'AI Vision & Strategy': {
#         'vision_not_in_strategy': {
#             'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q1 <= 2,
#             'meaning': 'Vision is strong but not anchored in enterprise strategy',
#             'nudge': 'Include AI explicitly in the corporate strategy and review it quarterly'
#         },
#         'metrics_without_plan': {
#             'condition': lambda q1, q2, q3, q4, q5: q3 >= 4 and q4 <= 2,
#             'meaning': 'KPIs exist, but there is no realistic plan to deliver',
#             'nudge': 'Publish a capacity-aligned quarterly roadmap with risks and owners'
#         },
#         'strategy_not_cascaded': {
#             'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q5 <= 2,
#             'meaning': 'Strategy exists but is not communicated or understood',
#             'nudge': 'Run quarterly all-hands and publish a narrative pack (one-pager, FAQ)'
#         },
#         'plan_not_socialized': {
#             'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q5 <= 2,
#             'meaning': 'A solid plan exists but is not broadly shared',
#             'nudge': 'Share the roadmap quarterly and tag BU dependencies and owners'
#         }
#     },
#     'Change Management & Adoption': {
#         'comms_without_strategy': {
#             'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q1 <= 2,
#             'meaning': 'You communicate well, but there\'s no change strategy—messages drift',
#             'nudge': 'Build a stakeholder-based change plan and align comms to it'
#         },
#         'training_without_comms': {
#             'condition': lambda q1, q2, q3, q4, q5: q3 >= 4 and q2 <= 2,
#             'meaning': 'Training is strong, but the core narrative is weak—confusion persists',
#             'nudge': 'Establish a consistent narrative and comms calendar'
#         },
#         'champions_without_training': {
#             'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q3 <= 2,
#             'meaning': 'Champions exist, but they lack enablement—support quality is uneven',
#             'nudge': 'Provide role-based training kits and job aids for champions'
#         },
#         'measurement_without_strategy': {
#             'condition': lambda q1, q2, q3, q4, q5: q5 >= 4 and q1 <= 2,
#             'meaning': 'You measure adoption, but there\'s no plan—data won\'t drive action',
#             'nudge': 'Tie KPIs and actions to a documented change plan'
#         },
#         'comms_without_measurement': {
#             'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q5 <= 2,
#             'meaning': 'Comms are strong, but success isn\'t measured—can\'t learn or improve',
#             'nudge': 'Add adoption dashboards, surveys, and action trackers'
#         }
#     },
#     'Customer Partner Ecosystem': {
#         'partners_without_customers': {
#             'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q1 <= 2,
#             'meaning': 'You have a solid partner strategy, but weak customer insight—offers may miss the mark',
#             'nudge': 'Run structured discovery (interviews, pilots, win/loss) and tie partner bets to demand signals'
#         },
#         'contracts_without_strategy': {
#             'condition': lambda q1, q2, q3, q4, q5: q3 >= 4 and q2 <= 2,
#             'meaning': 'Legal terms are mature, but partner strategy is unclear—misaligned commitments risk value',
#             'nudge': 'Define portfolio tiering and selection criteria before expanding contracts'
#         },
#         'delivery_without_contracts': {
#             'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q3 <= 2,
#             'meaning': 'You co-deliver well, but contracts/IP/privacy aren\'t firm—exposure risk',
#             'nudge': 'Standardize MSAs/DPAs with AI/IP clauses and approval playbooks'
#         },
#         'performance_without_delivery': {
#             'condition': lambda q1, q2, q3, q4, q5: q5 >= 4 and q4 <= 2,
#             'meaning': 'You run SLAs/QBRs, but joint delivery is weak—metrics won\'t translate to outcomes',
#             'nudge': 'Stand up co-sell kits, integration templates, and support readiness'
#         },
#         'customers_without_partners': {
#             'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q2 <= 2,
#             'meaning': 'Customer demand is validated, but partner strategy is missing—scale will stall',
#             'nudge': 'Build a tiered partner portfolio and due diligence to meet demand at scale'
#         }
#     }
# }

# # Category prioritization for strengths/opportunities
# CATEGORY_PRIORITY = {
#     'AI Vision & Strategy': 1,
#     'Leadership & Governance': 2,
#     'Operating Model & Funding': 3,
#     'Data Foundations & Quality': 4,
#     'Data Governance & Security': 5,
#     'Platform & Integration Architecture': 6,
#     'ML Lifecycle & Model Ops': 7,
#     'Portfolio & Value': 8,
#     'Talent & Culture': 9,
#     'Responsible AI & Risk': 10,
#     'Change Management & Adoption': 11,
#     'Customer Partner Ecosystem': 12
# }

# # Stage descriptions
# AI_VISION_STAGE_PARAS = {
#     'Nascent': 'AI direction is largely undefined. Focus first on a one-page North Star that states why AI matters, where value will come from, and who owns it. Establish a minimal KPI link for 2–3 priority initiatives and publish a working 12-month view to start aligning capacity.',
#     'Emerging': 'An AI vision exists in draft and is starting to guide decisions. Strengthen it by tying 2–3 enterprise outcomes to named KPIs and owners. Move from an idea list to a capacity-aware quarterly roadmap, and set a recurring review cadence to build trust in the plan.',
#     'Scaling': 'AI direction is clear enough to guide prioritization, and value signals are visible. Tighten KPI coverage across initiatives and shift to a predictable quarterly roadmap cadence. Broaden communication so teams can self-serve context and reduce escalations.',
#     'Transforming': 'Vision, KPIs, and a capacity-aligned roadmap are reviewed on cadence and used in decisions. Lean into consistency: keep scenarios current, surface risks early, and make metrics and FAQs easy to find across BUs to maintain alignment at scale.',
#     'Leading': 'AI is part of the enterprise narrative and planning rhythm. Outcomes, risks, and scenarios are actively managed, and teams can trace investments to the North Star. Sustain this by evolving the narrative as markets change and keeping KPI/roadmap hygiene impeccable.'
# }

# def get_maturity_stage(score):
#     """Get maturity stage based on score"""
#     if 5 <= score <= 9:
#         return 'Nascent'
#     elif 10 <= score <= 14:
#         return 'Emerging'
#     elif 15 <= score <= 19:
#         return 'Scaling'
#     elif 20 <= score <= 24:
#         return 'Transforming'
#     elif score == 25:
#         return 'Leading'
#     else:
#         return 'Nascent'

# def evaluate_category_rules(category, scores):
#     """Evaluate rules for a specific category"""
#     if category not in CATEGORY_RULES or category not in scores:
#         return []
    
#     category_scores = scores[category]
#     if len(category_scores) < 5:
#         return []
    
#     q1, q2, q3, q4, q5 = category_scores[:5]
#     triggered_rules = []
    
#     for rule_name, rule_data in CATEGORY_RULES[category].items():
#         if rule_data['condition'](q1, q2, q3, q4, q5):
#             triggered_rules.append({
#                 'category': category,
#                 'rule': rule_name,
#                 'meaning': rule_data['meaning'],
#                 'nudge': rule_data['nudge']
#             })
    
#     return triggered_rules

# def get_prioritized_categories(category_scores):
#     """Get top 3 strengths and opportunities based on scores and priority"""
#     sorted_categories = sorted(
#         category_scores.items(),
#         key=lambda x: (-x[1], CATEGORY_PRIORITY.get(x[0], 999))
#     )
    
#     strengths = sorted_categories[:3]
#     opportunities = sorted_categories[-3:]
#     opportunities.reverse()
    
#     return strengths, opportunities

# def evaluate_use_case_rules(scores):
#     """Evaluate all category rules and return triggered rules"""
#     all_triggered_rules = []
    
#     for category in scores.keys():
#         triggered_rules = evaluate_category_rules(category, scores)
#         all_triggered_rules.extend(triggered_rules)
    
#     return all_triggered_rules