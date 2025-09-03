##------------------------------------------------------------------------
# -------------------------------------------------------------
#  AI Maturity Assessment – UPDATED QUESTION BANK (Sept-2023)
#  9 Categories | 5 Questions per Category | 5-Point Scale
# -------------------------------------------------------------
ASSESSMENT_QUESTIONS = {

    # ------------------------------------------------------------------
    # 1. AI Vision & Strategic Alignment
    # ------------------------------------------------------------------
    "AI Vision & Strategic Alignment": {
        "Q1": {
            "question": "How clearly is AI embedded in your company’s long-term strategy?",
            "options": {
                "A": {"text": "AI is not a formal part of our business strategy",                          "score": 1},
                "B": {"text": "It’s occasionally mentioned, but not connected to outcomes",                "score": 2},
                "C": {"text": "Specific AI opportunities are being explored by some teams",                "score": 3},
                "D": {"text": "AI features in strategic initiatives at the departmental level",            "score": 4},
                "E": {"text": "AI is core to our strategic roadmap and long-term positioning",             "score": 5}
            }
        },
        "Q2": {
            "question": "Does your organization have a documented AI vision or strategic blueprint?",
            "options": {
                "A": {"text": "No formal AI vision or documentation exists",                               "score": 1},
                "B": {"text": "An informal vision exists in isolated functions",                           "score": 2},
                "C": {"text": "We’re drafting or validating an enterprise AI vision",                      "score": 3},
                "D": {"text": "A documented vision exists and guides key initiatives",                     "score": 4},
                "E": {"text": "Our AI vision is institutionalized and drives strategic priorities",        "score": 5}
            }
        },
        "Q3": {
            "question": "How tightly are AI initiatives linked to measurable business outcomes (e.g., revenue, cost, CX)?",
            "options": {
                "A": {"text": "AI projects are disconnected from business outcomes",                       "score": 1},
                "B": {"text": "Some pilots show promise but lack metrics",                                 "score": 2},
                "C": {"text": "Metrics are defined for high-priority use cases only",                      "score": 3},
                "D": {"text": "KPIs are actively tracked for most AI initiatives",                         "score": 4},
                "E": {"text": "Every AI investment is mapped to clear business impact",                    "score": 5}
            }
        },
        "Q4": {
            "question": "How is AI perceived by leadership — as a tool, or a business transformation enabler?",
            "options": {
                "A": {"text": "It’s not actively considered in leadership discussions",                    "score": 1},
                "B": {"text": "Seen mainly as a tech initiative or automation tool",                       "score": 2},
                "C": {"text": "Considered valuable for improving efficiency",                              "score": 3},
                "D": {"text": "Framed as a lever for digital transformation",                              "score": 4},
                "E": {"text": "Viewed as a core enabler of future business models",                        "score": 5}
            }
        },
        "Q5": {
            "question": "How well does your AI vision translate from strategy into execution at the product/service level?",
            "options": {
                "A": {"text": "There’s no evidence of AI vision shaping products or services",             "score": 1},
                "B": {"text": "A few pilots exist, but they aren’t tied back to strategy",                 "score": 2},
                "C": {"text": "Some offerings reflect AI strategy, though inconsistently",                 "score": 3},
                "D": {"text": "AI strategy is guiding multiple product/service initiatives",               "score": 4},
                "E": {"text": "AI vision consistently drives how we build and deliver products/services",  "score": 5}
            }
        }
    },

    # ------------------------------------------------------------------
    # 2. Leadership & Governance
    # ------------------------------------------------------------------
    "Leadership & Governance": {
        "Q1": {
            "question": "How aligned is your leadership team on the strategic importance of AI?",
            "options": {
                "A": {"text": "There is no clear leadership stance on AI",                                 "score": 1},
                "B": {"text": "One or two leaders are experimenting, but there’s no shared vision",        "score": 2},
                "C": {"text": "Most leaders recognize its potential, but direction is fragmented",         "score": 3},
                "D": {"text": "Senior leadership is aligned on AI’s strategic role",                      "score": 4},
                "E": {"text": "AI has unified leadership sponsorship and cross-functional buy-in",         "score": 5}
            }
        },
        "Q2": {
            "question": "Is there clear executive ownership for AI across the organization?",
            "options": {
                "A": {"text": "No one is formally accountable for AI",                                     "score": 1},
                "B": {"text": "Ownership is fragmented across functions or IT",                            "score": 2},
                "C": {"text": "A designated leader exists but lacks influence",                            "score": 3},
                "D": {"text": "A senior executive champions AI with mandate, budget, and authority",       "score": 4},
                "E": {"text": "AI ownership is embedded in Board/CEO oversight and governance",            "score": 5}
            }
        },
        "Q3": {
            "question": "How aligned are business and technology leaders in driving AI governance and outcomes?",
            "options": {
                "A": {"text": "Business and technical teams work in silos",                                "score": 1},
                "B": {"text": "Occasional collaboration on specific projects",                             "score": 2},
                "C": {"text": "Joint discussions happen during planning stages",                           "score": 3},
                "D": {"text": "Shared ownership and delivery exists in core use cases",                    "score": 4},
                "E": {"text": "Business and tech leaders co-own and co-deliver AI outcomes",              "score": 5}
            }
        },
        "Q4": {
            "question": "Are AI-related decisions guided by a formal governance process?",
            "options": {
                "A": {"text": "No formal process exists — decisions are ad hoc",                           "score": 1},
                "B": {"text": "Some guidelines exist, but are inconsistently applied",                     "score": 2},
                "C": {"text": "Governance is emerging for major initiatives",                              "score": 3},
                "D": {"text": "Formal governance exists for approvals, risk, and deployment",              "score": 4},
                "E": {"text": "AI governance is mature, transparent, and embedded into decision-making",   "score": 5}
            }
        },
        "Q5": {
            "question": "Is there an executive forum or steering committee that regularly reviews AI initiatives?",
            "options": {
                "A": {"text": "No such forum exists",                                                      "score": 1},
                "B": {"text": "Discussions happen sporadically during budget cycles",                      "score": 2},
                "C": {"text": "A working group reviews select AI initiatives",                             "score": 3},
                "D": {"text": "A steering committee actively monitors AI roadmap and risks",               "score": 4},
                "E": {"text": "AI oversight is institutionalized at the C-level or board level",           "score": 5}
            }
        }
    },

    # ------------------------------------------------------------------
    # 3. Use Case Portfolio & Prioritization
    # ------------------------------------------------------------------
    "Use Case Portfolio & Prioritization": {
        "Q1": {
            "question": "What is the current scale of AI adoption across your organization?",
            "options": {
                "A": {"text": "AI is not currently used in any business area",                             "score": 1},
                "B": {"text": "A few exploratory pilots are underway",                                     "score": 2},
                "C": {"text": "Multiple teams are running isolated use cases",                             "score": 3},
                "D": {"text": "Cross-functional adoption is growing with visible outcomes",                "score": 4},
                "E": {"text": "AI is embedded across core workflows and business functions",               "score": 5}
            }
        },
        "Q2": {
            "question": "How are AI use cases prioritized based on business value and feasibility?",
            "options": {
                "A": {"text": "No formal prioritization framework exists",                                 "score": 1},
                "B": {"text": "Use cases are selected based on individual interest or urgency",            "score": 2},
                "C": {"text": "Some prioritization happens based on ROI or resource need",                 "score": 3},
                "D": {"text": "Use cases are evaluated systematically across value, risk, feasibility",    "score": 4},
                "E": {"text": "A standardized, strategic prioritization model is used enterprise-wide",    "score": 5}
            }
        },
        "Q3": {
            "question": "Are use cases aligned with clear metrics or KPIs?",
            "options": {
                "A": {"text": "No KPIs are defined for AI projects",                                       "score": 1},
                "B": {"text": "Some pilots track output metrics (e.g., accuracy)",                         "score": 2},
                "C": {"text": "High-priority projects have defined success metrics",                       "score": 3},
                "D": {"text": "Most AI projects are tied to measurable business impact",                   "score": 4},
                "E": {"text": "All AI initiatives are driven by well-defined KPIs and monitored",          "score": 5}
            }
        },
        "Q4": {
            "question": "What is the success rate of AI pilots moving to production?",
            "options": {
                "A": {"text": "Most AI pilots do not move beyond experimentation",                         "score": 1},
                "B": {"text": "A few pilots transition to limited use",                                    "score": 2},
                "C": {"text": "Select use cases have scaled to stable deployments",                        "score": 3},
                "D": {"text": "Many pilots successfully convert to business-as-usual operations",          "score": 4},
                "E": {"text": "Strong track record of converting pilots to scalable production systems",   "score": 5}
            }
        },
        "Q5": {
            "question": "Are there playbooks or templates to accelerate repeatable AI use cases?",
            "options": {
                "A": {"text": "No playbooks or reusable assets exist",                                     "score": 1},
                "B": {"text": "Individual teams create their own ad-hoc approaches",                       "score": 2},
                "C": {"text": "Some templates are available but inconsistently applied",                   "score": 3},
                "D": {"text": "Shared playbooks exist for specific domains or use-case types",             "score": 4},
                "E": {"text": "Robust library of reusable AI assets and best practices is institutionalized","score": 5}
            }
        }
    },

    # ------------------------------------------------------------------
    # 4. Data Infrastructure & Quality
    # ------------------------------------------------------------------
    "Data Infrastructure & Quality": {
        "Q1": {
            "question": "How accessible is high-quality data for AI initiatives across your organization?",
            "options": {
                "A": {"text": "Data is difficult to locate or use for AI",                                 "score": 1},
                "B": {"text": "Data exists but is siloed, inconsistent, and poorly formatted",             "score": 2},
                "C": {"text": "Access is possible through manual data preparation",                        "score": 3},
                "D": {"text": "Unified data platforms make key data accessible",                           "score": 4},
                "E": {"text": "Real-time, governed, on-demand data is available enterprise-wide",          "score": 5}
            }
        },
        "Q2": {
            "question": "Does your organization maintain a data catalog or inventory to support AI?",
            "options": {
                "A": {"text": "No formal data catalog exists",                                             "score": 1},
                "B": {"text": "A catalog is being planned or piloted",                                     "score": 2},
                "C": {"text": "Catalogs exist for specific domains or teams",                              "score": 3},
                "D": {"text": "A searchable catalog covers most enterprise data",                          "score": 4},
                "E": {"text": "Dynamic, enterprise-wide catalog is fully integrated and updated",          "score": 5}
            }
        },
        "Q3": {
            "question": "Are internal and external data sources integrated to support AI models?",
            "options": {
                "A": {"text": "No integration efforts exist",                                              "score": 1},
                "B": {"text": "Ad-hoc connections are built when needed",                                  "score": 2},
                "C": {"text": "Integration exists in select AI projects",                                  "score": 3},
                "D": {"text": "Systematic pipelines ingest internal and external sources",                 "score": 4},
                "E": {"text": "Enterprise-wide, scalable architecture unifies data",                       "score": 5}
            }
        },
        "Q4": {
            "question": "How mature is your data infrastructure in supporting AI at scale?",
            "options": {
                "A": {"text": "Legacy systems and fragmented storage hinder AI workloads",                 "score": 1},
                "B": {"text": "Basic databases or warehouses exist but lack scalability",                  "score": 2},
                "C": {"text": "Department-level infrastructure supports some AI use cases",               "score": 3},
                "D": {"text": "Enterprise-grade infrastructure with governance supports major workloads",  "score": 4},
                "E": {"text": "Cloud-native, AI-ready architecture underpins enterprise-wide AI",          "score": 5}
            }
        },
        "Q5": {
            "question": "How confident are your teams in the quality of data used for AI?",
            "options": {
                "A": {"text": "Data quality is not measured or validated",                                 "score": 1},
                "B": {"text": "Quality varies widely across systems and sources",                          "score": 2},
                "C": {"text": "Validation exists for select high-priority data",                           "score": 3},
                "D": {"text": "Enterprise-wide quality checks and controls are in place",                 "score": 4},
                "E": {"text": "Data quality is proactively monitored and continuously improved",           "score": 5}
            }
        }
    },

    # ------------------------------------------------------------------
    # 5. Talent & Culture
    # ------------------------------------------------------------------
    "Talent & Culture": {
        "Q1": {
            "question": "Does your organization have in-house talent with AI/ML expertise?",
            "options": {
                "A": {"text": "No AI/ML talent is currently employed",                                     "score": 1},
                "B": {"text": "Limited to one or two data scientists or analysts",                         "score": 2},
                "C": {"text": "Small AI/ML team exists, supporting a few initiatives",                     "score": 3},
                "D": {"text": "Cross-functional teams include AI/ML specialists across departments",       "score": 4},
                "E": {"text": "AI/ML expertise is deeply embedded across business and tech units",         "score": 5}
            }
        },
        "Q2": {
            "question": "Are business teams being upskilled to work effectively with AI?",
            "options": {
                "A": {"text": "No formal upskilling programs in place",                                    "score": 1},
                "B": {"text": "Sporadic AI awareness sessions have been conducted",                        "score": 2},
                "C": {"text": "Select teams receive use-case-specific training",                           "score": 3},
                "D": {"text": "Ongoing learning programs exist for key functions",                         "score": 4},
                "E": {"text": "Structured AI literacy and enablement programs scaled org-wide",           "score": 5}
            }
        },
        "Q3": {
            "question": "Do business and technical teams collaborate fluidly on AI initiatives?",
            "options": {
                "A": {"text": "Business and tech teams work in isolation",                                 "score": 1},
                "B": {"text": "Collaboration is minimal, limited to handoffs",                             "score": 2},
                "C": {"text": "Some projects involve joint planning and review",                           "score": 3},
                "D": {"text": "AI initiatives are co-owned and co-executed across domains",               "score": 4},
                "E": {"text": "Cross-functional collaboration is embedded in how AI is built and scaled",  "score": 5}
            }
        },
        "Q4": {
            "question": "How structured is your operating model for delivering AI initiatives?",
            "options": {
                "A": {"text": "No defined structure — AI projects handled case by case",                   "score": 1},
                "B": {"text": "Work is assigned ad hoc, often outside core roles",                         "score": 2},
                "C": {"text": "Some functions have emerging AI roles or delivery structures",              "score": 3},
                "D": {"text": "Cross-functional operating model defines ownership for product, data, tech","score": 4},
                "E": {"text": "Enterprise-wide model institutionalizes accountability and governance",     "score": 5}
            }
        },
        "Q5": {
            "question": "Is there a culture that embraces experimentation, learning, and change with AI?",
            "options": {
                "A": {"text": "Culture is risk-averse and resistant to change",                            "score": 1},
                "B": {"text": "Experimentation happens occasionally, but only in isolated teams",          "score": 2},
                "C": {"text": "Some teams are encouraged to explore AI use cases",                         "score": 3},
                "D": {"text": "Fail-fast experimentation is promoted in innovation/digital units",         "score": 4},
                "E": {"text": "Growth mindset and test-and-learn approach is rewarded enterprise-wide",    "score": 5}
            }
        }
    },

    # ------------------------------------------------------------------
    # 6. Responsible AI & Risk
    # ------------------------------------------------------------------
    "Responsible AI & Risk": {
        "Q1": {
            "question": "Does your organization have a clear policy or framework for Responsible AI?",
            "options": {
                "A": {"text": "No formal principles or policies exist",                                    "score": 1},
                "B": {"text": "Ethical AI is discussed but not formalized",                                "score": 2},
                "C": {"text": "Draft guidelines are being reviewed",                                       "score": 3},
                "D": {"text": "Responsible AI policy is approved and shared",                              "score": 4},
                "E": {"text": "Responsible AI principles are codified and embedded into workflows",        "score": 5}
            }
        },
        "Q2": {
            "question": "Are AI models evaluated for bias, fairness, or unintended consequences?",
            "options": {
                "A": {"text": "No evaluations are conducted",                                              "score": 1},
                "B": {"text": "Basic fairness checks happen during development for select models",         "score": 2},
                "C": {"text": "Bias and fairness testing occurs in high-priority use cases",               "score": 3},
                "D": {"text": "Standardized evaluation protocols are applied across most AI initiatives",  "score": 4},
                "E": {"text": "Bias/fairness reviews are automated across the full AI lifecycle",          "score": 5}
            }
        },
        "Q3": {
            "question": "What oversight process governs AI deployment decisions?",
            "options": {
                "A": {"text": "No oversight process — deployment decisions are ad hoc",                    "score": 1},
                "B": {"text": "Deployment requires sign-off from project teams only",                      "score": 2},
                "C": {"text": "Critical models reviewed by designated leaders case by case",               "score": 3},
                "D": {"text": "Cross-functional governance exists for high-impact or regulated models",    "score": 4},
                "E": {"text": "Formal enterprise board evaluates and monitors all AI deployments",         "score": 5}
            }
        },
        "Q4": {
            "question": "How is accountability ensured for AI-driven decisions that impact users and stakeholders?",
            "options": {
                "A": {"text": "No accountability mechanisms exist",                                        "score": 1},
                "B": {"text": "Responsibility is unclear and handled reactively",                          "score": 2},
                "C": {"text": "Critical AI decisions have designated owners or review processes",          "score": 3},
                "D": {"text": "Most AI decisions tied to clear accountability and escalation paths",       "score": 4},
                "E": {"text": "Standardized ownership, oversight, and remediation across all AI systems",  "score": 5}
            }
        },
        "Q5": {
            "question": "What controls are in place to monitor and mitigate model risk (e.g., drift, performance, compliance)?",
            "options": {
                "A": {"text": "No model risk controls exist",                                              "score": 1},
                "B": {"text": "Risks addressed reactively after failures or issues",                       "score": 2},
                "C": {"text": "Some projects have validation and mitigation plans",                        "score": 3},
                "D": {"text": "Monitoring tools track performance, drift, and compliance for key models",  "score": 4},
                "E": {"text": "Enterprise-wide model risk management is systematic and proactive",         "score": 5}
            }
        }
    },

    # ------------------------------------------------------------------
    # 7. Measurement, Scaling & ROI
    # ------------------------------------------------------------------
    "Measurement, Scaling & ROI": {
        "Q1": {
            "question": "Do you measure the ROI of AI initiatives?",
            "options": {
                "A": {"text": "ROI is not currently tracked",                                              "score": 1},
                "B": {"text": "Success is gauged qualitatively or informally",                             "score": 2},
                "C": {"text": "ROI is estimated after pilots or PoCs",                                     "score": 3},
                "D": {"text": "ROI targets are defined and aligned with business KPIs",                    "score": 4},
                "E": {"text": "Every AI initiative follows a standardized ROI framework",                  "score": 5}
            }
        },
        "Q2": {
            "question": "Are AI initiatives tied to cost savings, revenue uplift, or customer experience?",
            "options": {
                "A": {"text": "No formal link between AI and outcomes",                                    "score": 1},
                "B": {"text": "Some anecdotal wins have been shared",                                      "score": 2},
                "C": {"text": "Isolated use cases show measurable outcomes",                               "score": 3},
                "D": {"text": "Most AI initiatives report against defined outcomes",                       "score": 4},
                "E": {"text": "Every AI use case tagged to core vectors (Growth, Cost, Risk, CX, etc.)",   "score": 5}
            }
        },
        "Q3": {
            "question": "How is AI performance and adoption tracked across the company?",
            "options": {
                "A": {"text": "No monitoring or tracking exists",                                          "score": 1},
                "B": {"text": "Teams track AI pilots manually in spreadsheets",                            "score": 2},
                "C": {"text": "Individual dashboards exist but limited in scope",                          "score": 3},
                "D": {"text": "Department-level dashboards track adoption and performance",                "score": 4},
                "E": {"text": "Enterprise-wide scorecards provide real-time visibility for executives",    "score": 5}
            }
        },
        "Q4": {
            "question": "How are insights from failed or under-performing AI initiatives captured and applied?",
            "options": {
                "A": {"text": "Failed initiatives are not revisited",                                      "score": 1},
                "B": {"text": "Teams occasionally reflect on what went wrong",                             "score": 2},
                "C": {"text": "Post-mortems are held for critical PoCs",                                   "score": 3},
                "D": {"text": "Insights from failures are documented and shared",                          "score": 4},
                "E": {"text": "Lessons systematically shape future AI design and governance",              "score": 5}
            }
        },
        "Q5": {
            "question": "Is there a scaling playbook for successful AI use cases?",
            "options": {
                "A": {"text": "No reusable process exists for scaling AI",                                 "score": 1},
                "B": {"text": "Select teams document learnings informally",                                "score": 2},
                "C": {"text": "Some pilots are translated into guides for reuse",                          "score": 3},
                "D": {"text": "Playbooks and SOPs help scale successful use cases",                        "score": 4},
                "E": {"text": "Enterprise-wide scaling playbook governs reuse, rollout, and integration",  "score": 5}
            }
        }
    },

    # ------------------------------------------------------------------
    # 8. Operating Model & Change Readiness
    # ------------------------------------------------------------------
    "Operating Model & Change Readiness": {
        "Q1": {
            "question": "How clearly defined is your AI operating model (ownership, delivery, and scale)?",
            "options": {
                "A": {"text": "No defined AI operating model exists",                                      "score": 1},
                "B": {"text": "Roles and responsibilities are unclear or scattered",                       "score": 2},
                "C": {"text": "A central AI/ML team or CoE operates in isolation",                         "score": 3},
                "D": {"text": "A federated model is emerging with shared responsibilities",                "score": 4},
                "E": {"text": "Enterprise-wide model aligns value delivery, ownership, and scale",         "score": 5}
            }
        },
        "Q2": {
            "question": "Are change management strategies in place to support AI adoption?",
            "options": {
                "A": {"text": "Change management is not addressed",                                        "score": 1},
                "B": {"text": "Communication is ad hoc, triggered only when challenges arise",            "score": 2},
                "C": {"text": "Awareness or training programs exist but are one-off",                      "score": 3},
                "D": {"text": "Change and enablement are embedded into most AI programs",                  "score": 4},
                "E": {"text": "Proactive change management integrated into every AI initiative",           "score": 5}
            }
        },
        "Q3": {
            "question": "Are business units incentivized to adopt AI solutions?",
            "options": {
                "A": {"text": "There are no incentives to use AI tools",                                   "score": 1},
                "B": {"text": "AI adoption is encouraged but lacks supporting mechanisms",                 "score": 2},
                "C": {"text": "Some teams get budget relief or productivity credits",                      "score": 3},
                "D": {"text": "AI adoption is embedded into team OKRs or KPIs",                            "score": 4},
                "E": {"text": "Incentives are directly linked to performance metrics and impact",          "score": 5}
            }
        },
        "Q4": {
            "question": "How are internal advocates or champions driving AI adoption?",
            "options": {
                "A": {"text": "No internal advocates or champions exist",                                  "score": 1},
                "B": {"text": "A few employees act as informal AI ambassadors",                            "score": 2},
                "C": {"text": "Formal AI champions exist in select teams or units",                        "score": 3},
                "D": {"text": "AI champions are designated across departments to drive adoption",          "score": 4},
                "E": {"text": "Cross-functional team leads awareness, communication, and adoption",        "score": 5}
            }
        },
        "Q5": {
            "question": "Do your teams have access to internal AI sandboxes or experimentation environments?",
            "options": {
                "A": {"text": "No experimentation environments exist",                                     "score": 1},
                "B": {"text": "Only technical teams can experiment with AI",                               "score": 2},
                "C": {"text": "Shared sandboxes exist in select departments",                              "score": 3},
                "D": {"text": "Business teams are encouraged to explore in open-access sandboxes",         "score": 4},
                "E": {"text": "Enterprise-funded sandboxes are governed and tied to innovation",           "score": 5}
            }
        }
    },

    # ------------------------------------------------------------------
    # 9. Technology & AI Infrastructure
    # ------------------------------------------------------------------
    "Technology & AI Infrastructure": {
        "Q1": {
            "question": "Does your infrastructure reliably support AI development and deployment?",
            "options": {
                "A": {"text": "No AI-ready infrastructure exists",                                         "score": 1},
                "B": {"text": "Experimental environments exist for limited testing",                       "score": 2},
                "C": {"text": "Dedicated servers or cloud instances are available for model training",     "score": 3},
                "D": {"text": "Scalable infrastructure supports enterprise-grade AI workloads",            "score": 4},
                "E": {"text": "Stack is optimized for GenAI, real-time AI, and multi-model orchestration", "score": 5}
            }
        },
        "Q2": {
            "question": "Are you using MLOps or AIOps tools to operationalize the AI lifecycle?",
            "options": {
                "A": {"text": "No operational tools or processes exist",                                   "score": 1},
                "B": {"text": "Scripts and workflows are managed manually",                                "score": 2},
                "C": {"text": "Tools are being piloted or adopted informally",                             "score": 3},
                "D": {"text": "Established tools like MLflow, SageMaker, or Vertex AI are in use",         "score": 4},
                "E": {"text": "Model lifecycle is fully automated end-to-end",                             "score": 5}
            }
        },
        "Q3": {
            "question": "Are AI models version-controlled, reproducible, and traceable across deployments?",
            "options": {
                "A": {"text": "No formal version control for models",                                      "score": 1},
                "B": {"text": "Manual documentation exists for select models",                             "score": 2},
                "C": {"text": "Versioning tools are used in limited projects",                             "score": 3},
                "D": {"text": "All models tracked and reproducible with audit trails",                     "score": 4},
                "E": {"text": "Full lineage, rollback, and auditability exist enterprise-wide",            "score": 5}
            }
        },
        "Q4": {
            "question": "Can your tech environment support real-time or near-real-time AI use cases?",
            "options": {
                "A": {"text": "No support for streaming or real-time capabilities",                        "score": 1},
                "B": {"text": "Basic pipelines exist for near-real-time but lack scalability",             "score": 2},
                "C": {"text": "Limited real-time models are in testing or production",                     "score": 3},
                "D": {"text": "Multiple real-time AI use cases are operational across functions",          "score": 4},
                "E": {"text": "Real-time inference and data streaming are core to AI system design",       "score": 5}
            }
        },
        "Q5": {
            "question": "Are AI models actively monitored for performance, drift, and reliability post-deployment?",
            "options": {
                "A": {"text": "No monitoring processes exist",                                             "score": 1},
                "B": {"text": "Monitoring happens manually and inconsistently",                            "score": 2},
                "C": {"text": "Dashboards and alerts are available for select models",                     "score": 3},
                "D": {"text": "Performance metrics and drift detection are partially automated",           "score": 4},
                "E": {"text": "End-to-end monitoring with automated retraining pipelines is standardized", "score": 5}
            }
        }
    }
}

# Category rules for identifying contradictions
CATEGORY_RULES = {
    'AI Vision & Strategic Alignment': {
        'vision_not_in_strategy': {
            'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q1 <= 2,
            'meaning': 'Vision is strong but not anchored in enterprise strategy',
            'nudge': 'Integrate the AI vision into the corporate strategy and ensure it is reviewed in quarterly leadership meetings'
        },
        'metrics_without_plan': {
            'condition': lambda q1, q2, q3, q4, q5: q3 >= 4 and q4 <= 2,
            'meaning': 'Strong measurement practices exist, but leadership still treats AI as a tech tool rather than a transformation lever.',
            'nudge': 'Conduct leadership workshops to reframe AI as a business model enabler, not just a technology initiative.'
        },
        'strategy_not_cascaded': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q5 <= 2,
            'meaning': 'AI is positioned strategically, but this hasn’t translated into products or services.',
            'nudge': 'Launch cross-functional “AI-in-innovation” pilots to bring strategy into tangible execution.'
        },
        'plan_not_socialized': {
            'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q5 <= 2,
            'meaning': 'A solid AI vision exists, but it hasn’t filtered into how offerings are designed or delivered.',
            'nudge': 'Publish a quarterly roadmap and run innovation roadshows with product and service teams.'
        },
        'ambition_without_outcomes': {
            'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q3 <= 2,
            'meaning': 'Leadership ambition is high, but there’s no evidence of AI linked to business outcomes.',
            'nudge': 'Define a business-outcome playbook linking each AI initiative to cost, growth, CX, or risk KPIs.'
        },
        'innovation_gap': {
            'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q5 <= 2,
            'meaning': 'Leadership frames AI as transformational, but innovation pipelines don’t reflect it.',
            'nudge': 'Embed AI checkpoints into product/service lifecycle gates (concept, design, launch).'
        }
    },
    'Leadership & Governance': {
        'many_without_focus': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q2 <= 2,
            'meaning': 'The organization has identified many AI use cases across functions, but without a prioritization framework. This creates scattered pilots and wasted effort — a “proof-of-concept graveyard.”',
            'nudge': 'Introduce a prioritization framework that scores use cases by business value, feasibility, and strategic alignment. Focus resources on the top 3–5 to maximize impact.'
        },
        'framework_without_pipeline': {
            'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q1 <= 2,
            'meaning': 'A strong prioritization framework exists, but the actual pipeline of AI use cases is thin. The organization is over-structuring without first generating enough opportunities to evaluate.',
            'nudge': 'Stimulate a healthy pipeline through business-unit ideation workshops, hackathons, and bottom-up submissions, so the framework has real use cases to filter.'
        },
        'pipeline_without_delivery': {
            'condition': lambda q1, q2, q3, q4, q5: q3 >= 4 and q4 <= 2,
            'meaning': 'A robust list of opportunities has been identified, but weak execution means few pilots successfully move to production. This signals an “ideas vs. delivery gap.”',
            'nudge': 'Build a pilot-to-production playbook with clear stage-gates, delivery owners, and MLOps processes to ensure ideas translate into business-ready solutions.'
        },
        'pilots_without_scaling': {
            'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q5 <= 2,
            'meaning': 'Pilots are being executed rigorously, but they rarely scale into repeatable, enterprise-wide solutions. This shows a structural barrier between experimentation and industrialization.',
            'nudge': 'Invest in scaling enablers like reusable templates, model registries, shared data pipelines, and governance that mandates every pilot includes a scaling roadmap.'
        },
        'wins_without_renewal': {
            'condition': lambda q1, q2, q3, q4, q5: q5 >= 4 and q2 <= 2,
            'meaning': 'Some use cases have successfully scaled, but there is no systematic process for refreshing the portfolio or linking it back to evolving business priorities. This creates stagnation and erodes long-term relevance.',
            'nudge': 'Institutionalize portfolio refresh by reviewing use cases quarterly, linking them to enterprise strategy, and rotating business sponsors to sustain momentum.'
        }
    },
    'Use Case Portfolio & Prioritization': {
        'pilots_stuck': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 3 and q4 <= 2,
            'meaning': 'Multiple pilots are active, but very few are transitioning to production. This creates "pilot purgatory," where effort doesn’t translate into business value.',
            'nudge': 'Introduce a standardized production-readiness checklist and governance gates to ensure pilots can scale.'
        },
        'value_without_framework': {
            'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q5 <= 2,
            'meaning': 'Use cases are being evaluated systematically, but reusable assets and playbooks are missing — slowing replication and scale.',
            'nudge': 'Build a central repository of playbooks, templates, and accelerators to make AI adoption repeatable.'
        },
        'metrics_without_scale': {
            'condition': lambda q1, q2, q3, q4, q5: q3 >= 4 and q4 <= 2,
            'meaning': 'Strong KPI alignment exists, but pilots rarely convert into production, meaning impact remains theoretical.',
            'nudge': 'Establish a “metrics-to-scale” pipeline, where only KPI-backed pilots are given resources to scale.'
        },
        'adoption_without_alignment': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q2 <= 2,
            'meaning': 'AI adoption is growing across functions, but prioritization is ad hoc — leading to duplication and diluted value.',
            'nudge': 'Deploy an enterprise prioritization framework tied to business strategy and risk appetite.'
        },
        'scale_without_reuse': {
            'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q5 <= 2,
            'meaning': 'Pilots are scaling successfully, but there are no reusable frameworks to repeat success across other teams.',
            'nudge': 'Codify successful use cases into enterprise playbooks and embed them into the AI lifecycle.'
        },
        'ambition_without_metrics': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q3 <= 2,
            'meaning': 'AI adoption is visible, but projects lack metrics or KPIs — risking wasted investment.',
            'nudge': 'Link every AI use case to at least one cost, growth, CX, or risk KPI before greenlighting.'
        }
    },
    'Data Infrastructure & Quality': {
        'access_without_quality': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q5 <= 2,
            'meaning': 'Data is technically accessible through unified platforms, but quality remains poor — meaning teams don’t trust or use it effectively.',
            'nudge': 'Establish enterprise-wide data quality standards and automate validation/cleansing to build confidence in available data.'
        },
        'catalog_without_integration': {
            'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q3 <= 2,
            'meaning': 'A strong catalog or inventory exists, but data sources aren’t integrated — users can “find” data but not use it holistically.',
            'nudge': 'Expand catalog adoption by embedding integration pipelines that link data sources into a usable enterprise architecture.'
        },
        'infra_without_catalog': {
            'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q2 <= 2,
            'meaning': 'Infrastructure is enterprise-grade, but no catalog exists — meaning users still struggle to locate and consume data.',
            'nudge': 'Build a dynamic data catalog with metadata, lineage, and self-service search to maximize infrastructure value.'
        },
        'integration_without_scale': {
            'condition': lambda q1, q2, q3, q4, q5: q3 >= 4 and q4 <= 2,
            'meaning': 'Data integration pipelines exist, but infrastructure isn’t mature enough to support AI at scale — creating performance bottlenecks.',
            'nudge': 'Upgrade to cloud-native or hybrid architectures designed to handle advanced AI workloads at enterprise scale.'
        },
        'quality_without_access': {
            'condition': lambda q1, q2, q3, q4, q5: q5 >= 4 and q1 <= 2,
            'meaning': 'Data quality processes are strong, but teams struggle to access data efficiently. This creates wasted potential.',
            'nudge': 'Invest in democratized access layers and self-service data platforms to make trusted data usable by all teams.'
        },
        'infra_without_quality': {
            'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q5 <= 2,
            'meaning': 'Enterprise infrastructure is in place, but poor quality undermines reliability — “garbage in, garbage out.”',
            'nudge': 'Embed continuous monitoring, data lineage, and automated error detection directly into the infrastructure.'
        }
    },
    'Talent & Culture': {
        'talent_without_upskilling': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 3 and q2 <= 2,
            'meaning': 'In-house AI expertise exists, but business teams aren’t being upskilled — leading to dependency on specialists.',
            'nudge': 'Launch structured AI literacy programs so business users can effectively collaborate with technical teams.'
        },
        'collaboration_gap': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 3 and q3 <= 2,
            'meaning': 'AI specialists exist, but collaboration with business teams is weak, creating silos and handoffs.',
            'nudge': 'Establish cross-functional squads where AI experts and business owners co-own initiatives.'
        },
        'roles_without_culture': {
            'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q5 <= 2,
            'meaning': 'Operating model is structured, but the culture resists experimentation — limiting innovation.',
            'nudge': 'Embed AI change agents, run safe-to-fail pilots, and reward test-and-learn behaviors.'
        },
        'upskilling_without_roles': {
            'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q4 <= 2,
            'meaning': 'Teams are being trained, but there’s no structured operating model to apply their skills.',
            'nudge': 'Define AI roles and delivery structures to ensure new skills translate into impact.'
        },
        'culture_without_talent': {
            'condition': lambda q1, q2, q3, q4, q5: q5 >= 4 and q1 <= 2,
            'meaning': 'Culture supports experimentation, but there’s no AI talent to execute — leading to stalled progress.',
            'nudge': 'Hire foundational AI/ML talent and create a pipeline of technical experts to match cultural ambition.'
        },
        'structure_without_collaboration': {
            'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q3 <= 2,
            'meaning': 'An operating model exists, but business–tech collaboration is minimal, making execution inefficient.',
            'nudge': 'Redesign delivery models to enforce joint accountability between business and technical teams.'
        }
    },
    'Responsible AI & Risk': {
        'policy_without_action': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q2 <= 2,
            'meaning': 'A Responsible AI policy exists, but it isn’t backed by active fairness or bias evaluations.',
            'nudge': 'Move from principles to practice — operationalize your policy with standardized fairness and risk reviews in every project.'
        },
        'oversight_without_accountability': {
            'condition': lambda q1, q2, q3, q4, q5: q3 >= 4 and q4 <= 2,
            'meaning': 'Strong governance exists for approving deployments, but accountability for decisions impacting users is unclear.',
            'nudge': 'Tie every AI system to a designated owner with clear escalation and remediation processes.'
        },
        'accountability_without_controls': {
            'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q5 <= 2,
            'meaning': 'Accountability structures are in place, but no risk monitoring or controls exist — meaning owners are responsible without tools to manage risks.',
            'nudge': 'Implement monitoring frameworks for drift, compliance, and misuse so accountability translates into action.'
        },
        'controls_without_policy': {
            'condition': lambda q1, q2, q3, q4, q5: q5 >= 4 and q1 <= 2,
            'meaning': 'Strong risk controls exist, but there is no overarching Responsible AI policy to unify them.',
            'nudge': 'Formalize an enterprise-wide Responsible AI framework to guide risk practices consistently.'
        },
        'fairness_without_oversight': {
            'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q3 <= 2,
            'meaning': 'Bias and fairness checks are conducted, but there is no formal oversight for approving or monitoring deployments.',
            'nudge': 'Introduce governance boards or review committees to ensure fairness findings are enforced.'
        },
        'policy_without_transparency': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q4 <= 2,
            'meaning': 'A Responsible AI policy exists, but AI-driven decisions remain opaque to users and stakeholders.',
            'nudge': 'Embed transparency measures (decision logs, disclosures, user-facing explanations) as mandatory elements of the policy.'
        }
    },
    'Measurement, Scaling & ROI': {
        'outcomes_without_roi': {
            'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q1 <= 2,
            'meaning': 'AI initiatives are tied to outcomes, but ROI isn’t formally measured — meaning benefits are anecdotal, not proven.',
            'nudge': 'Introduce a standardized ROI framework that translates outcomes into financial and strategic impact.'
        },
        'dashboards_without_learning': {
            'condition': lambda q1, q2, q3, q4, q5: q3 >= 4 and q4 <= 2,
            'meaning': 'Dashboards track adoption and performance, but lessons from failed initiatives are not systematically applied.',
            'nudge': 'Establish structured post-mortems and integrate learnings into governance and portfolio reviews.'
        },
        'scaling_without_measurement': {
            'condition': lambda q1, q2, q3, q4, q5: q5 >= 4 and q1 <= 2,
            'meaning': 'Playbooks exist to scale AI, but ROI is not tracked — making it impossible to prove value at scale.',
            'nudge': 'Tie scaling playbooks to ROI checkpoints and outcome metrics before rollout.'
        },
        'roi_without_outcomes': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q2 <= 2,
            'meaning': 'ROI frameworks exist, but AI projects are not tied to core business outcomes — risking misaligned investments.',
            'nudge': 'Ensure every ROI framework explicitly maps to growth, cost, CX, sustainability, risk, or data vectors.'
        },
        'scaling_without_tracking': {
            'condition': lambda q1, q2, q3, q4, q5: q5 >= 4 and q3 <= 2,
            'meaning': 'A scaling playbook exists, but performance/adoption is not centrally tracked — creating blind spots.',
            'nudge': 'Connect scaling frameworks to enterprise dashboards and executive scorecards for visibility.'
        },
        'learning_without_scaling': {
            'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q5 <= 2,
            'meaning': 'Lessons from failures are captured, but they are not institutionalized into scaling frameworks.',
            'nudge': 'Embed feedback loops into scaling playbooks so learnings systematically improve reuse and rollout.'
        }
    },
    'AI Operating Model & Change Readiness': {
        'model_without_change': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q2 <= 2,
            'meaning': 'A structured operating model exists, but change management is weak — adoption risks stalling.',
            'nudge': 'Integrate change enablement into every AI initiative, with communication, training, and support built from the start.'
        },
        'incentives_without_structure': {
            'condition': lambda q1, q2, q3, q4, q5: q3 >= 4 and q1 <= 2,
            'meaning': 'Business units are incentivized to adopt AI, but no operating model defines ownership or delivery.',
            'nudge': 'Establish an enterprise AI operating model so incentives lead to sustainable adoption, not fragmented efforts.'
        },
        'champions_without_support': {
            'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q1 <= 2,
            'meaning': 'Champions exist across departments, but without structured change management, their influence is limited.',
            'nudge': 'Provide AI champions with playbooks, training resources, and leadership backing to scale their impact.'
        },
        'sandboxes_without_model': {
            'condition': lambda q1, q2, q3, q4, q5: q5 >= 4 and q2 <= 2,
            'meaning': 'Experimentation environments exist, but no operating model guides how pilots translate into business adoption.',
            'nudge': 'Link sandbox experiments into the operating model and scaling framework to ensure learnings drive enterprise value.'
        },
        'sandbox_without_backbone': {
            'condition': lambda q1, q2, q3, q4, q5: q5 >= 4 and q1 <= 2,
            'meaning': 'Sandboxes exist and business teams can experiment, but there’s no operating model to scale learnings.',
            'nudge': 'Establish governance and ownership so experimentation feeds into enterprise adoption.'
        },
        'structure_without_incentives': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q3 <= 2,
            'meaning': 'A formal operating model exists, but business units are not incentivized to adopt AI → structure risks becoming theoretical.',
            'nudge': 'Link AI adoption explicitly to team OKRs and business outcomes to ensure usage takes root.'
        }
    },
    'Technology & AI Infrastructure': {
        'infra_without_ops': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q2 <= 2,
            'meaning': 'Scalable infrastructure exists, but there are no MLOps/AIOps practices — making AI hard to operationalize.',
            'nudge': 'Introduce standardized MLOps pipelines to automate training, deployment, and monitoring, ensuring infrastructure delivers value.'
        },
        'ops_without_monitoring': {
            'condition': lambda q1, q2, q3, q4, q5: q2 >= 4 and q5 <= 2,
            'meaning': 'MLOps tools are in place, but deployed models are not actively monitored — creating blind spots post-launch.',
            'nudge': 'Extend MLOps pipelines with automated monitoring and drift detection to close the loop on model reliability.'
        },
        'infra_without_traceability': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q3 <= 2,
            'meaning': 'Infrastructure is strong, but models lack versioning or traceability — risking compliance and reproducibility issues.',
            'nudge': 'Implement enterprise-wide model version control, audit trails, and rollback mechanisms.'
        },
        'realtime_without_infra': {
            'condition': lambda q1, q2, q3, q4, q5: q4 >= 4 and q1 <= 2,
            'meaning': 'Real-time models are in use, but core infrastructure is not AI-ready — creating fragility.',
            'nudge': 'Upgrade infrastructure to cloud-native, scalable architectures designed for streaming and real-time AI.'
        },
        'monitoring_without_governance': {
            'condition': lambda q1, q2, q3, q4, q5: q5 >= 4 and q3 <= 2,
            'meaning': 'Models are monitored for drift and performance, but there’s no versioning or traceability.',
            'nudge': 'Pair monitoring with full lineage and governance frameworks to ensure accountability.'
        },
        'infra_without_realtime': {
            'condition': lambda q1, q2, q3, q4, q5: q1 >= 4 and q4 <= 2,
            'meaning': 'Infrastructure is enterprise-grade, but real-time AI support is absent — limiting advanced use cases.',
            'nudge': 'Embed real-time inference and streaming capabilities into the architecture to unlock next-gen AI adoption.'
        }
    }
}

# Category prioritization
CATEGORY_PRIORITY = {
    'AI Vision & Strategic Alignment': 1,
    'Leadership & Governance': 2,
    'Data Infrastructure & Quality': 3,
    'Technology & AI Infrastructure': 4,
    'Use Case Portfolio & Prioritization': 5,
    'Measurement, Scaling & ROI': 6,
    'Talent & Culture': 7,
    'Operating Model & Change Readiness': 8,
    'Responsible AI & Risk': 9
}

def get_maturity_stage_from_25_scale(stage_score):
    """Get maturity stage based on 25-point scale"""
    if 5 <= stage_score < 10:
        return 'Nascent'
    elif 10 <= stage_score < 15:
        return 'Emerging'
    elif 15 <= stage_score < 20:
        return 'Scaling'
    elif 20 <= stage_score < 25:
        return 'Transforming'
    elif stage_score >= 25:
        return 'Leading'
    else:
        return 'Nascent'  # For scores below 5

def calculate_category_score(responses):
    """Calculate total score and average for a category"""
    total_score = sum(responses)
    average_score = total_score / len(responses) if responses else 0
    return total_score, round(average_score, 1)

def evaluate_category_rules(category, scores):
    """Evaluate rules for a specific category"""
    if category not in CATEGORY_RULES or len(scores) < 5:
        return []
    
    q1, q2, q3, q4, q5 = scores[:5]
    triggered_rules = []
    
    for rule_name, rule_data in CATEGORY_RULES[category].items():
        if rule_data['condition'](q1, q2, q3, q4, q5):
            triggered_rules.append({
                'category': category,
                'rule': rule_name,
                'meaning': rule_data['meaning'],
                'nudge': rule_data['nudge']
            })
    
    return triggered_rules

def evaluate_use_case_rules(scores):
    """Evaluate all category rules and return triggered rules"""
    all_triggered_rules = []
    
    for category in scores.keys():
        triggered_rules = evaluate_category_rules(category, scores[category])
        all_triggered_rules.extend(triggered_rules)
    
    return all_triggered_rules

def get_prioritized_categories(category_scores):
    """Get top 3 strengths and opportunities based on scores and priority"""
    sorted_categories = sorted(
        category_scores.items(),
        key=lambda x: (-x[1], CATEGORY_PRIORITY.get(x[0], 999))
    )
    
    strengths = sorted_categories[:3]
    opportunities = sorted_categories[-3:]
    opportunities.reverse()
    
    return strengths, opportunities

# Stage descriptions
AI_VISION_STAGE_PARAS = {
    'Nascent': 'AI maturity is at a foundational low. The organization lacks a defined AI strategy, use cases are absent or uncoordinated, and no operating model exists. Data is siloed, inconsistent, and largely unusable for AI. Technology environments are outdated, with no support for scaling AI models. Talent is missing or limited to isolated enthusiasts, with no culture of experimentation. Governance, responsible AI, and risk management are nonexistent. No ROI or business value is measured, leaving AI disconnected from business priorities.',
    'Emerging': 'The organization has started dipping its toes into AI. Pilots and proofs of concept exist, often in silos, but adoption is fragmented and not prioritized by value. A basic data foundation or catalog is forming, but accessibility and quality remain barriers. Tech infra supports only small-scale experiments. A handful of AI/ML specialists or external partners provide expertise, but business teams are not yet upskilled. Change management and incentives are absent or inconsistent. Governance is minimal — policies may be drafted but not enforced. ROI is anecdotal at best, with no systematic link to cost, growth, or customer outcomes.',
    'Scaling': 'AI is producing repeatable wins across functions, with multiple use cases moving to production. Use case prioritization frameworks exist, and most high-value projects are tied to KPIs. Data infrastructure is maturing — warehouses or unified platforms exist, though not always enterprise-wide. Technology supports model training and deployment, with some MLOps in place. Talent pools are growing, and business teams receive targeted training, but cultural readiness varies. Change management is active in most initiatives, and incentives for adoption are starting to appear. Governance and responsible AI are formalizing, though often reactive. ROI is measured for select initiatives, and scaling playbooks are emerging.',
    'Transforming': 'AI has become a strategic enabler of business transformation. Use cases are systematically prioritized, tied to ROI, and linked to strategic vectors like Growth, Cost, Risk, CX, or Sustainability. Data platforms are enterprise-wide, governed, and support near-real-time access. AI infrastructure is scalable, with advanced MLOps enabling reproducibility, monitoring, and drift detection. Talent is embedded across functions, with structured upskilling and cross-functional collaboration. Change management is proactive, supported by champions, incentives, and sandboxes for experimentation. Responsible AI frameworks are codified, with oversight boards and bias reviews in place. ROI is tracked enterprise-wide, with dashboards and post-mortems driving continuous improvement. The organization adapts lessons from both successes and failures, embedding AI into its operating DNA.',
    'Leading': 'AI is institutionalized as a competitive advantage. The enterprise has a clear AI operating model, with accountability, governance, and value delivery standardized across all functions. Use cases are continuously refreshed and prioritized, linked directly to business outcomes. Data is real-time, governed, and AI-ready, fueling advanced analytics and generative AI at scale. Technology is cutting-edge — cloud-native, orchestrating multi-model systems, real-time inference, and automation. Talent and culture are enterprise-wide strengths: business and tech teams collaborate seamlessly, and AI fluency is part of the organizational DNA. Change management is anticipatory, not reactive, with incentives and champions embedded everywhere. Responsible AI is operationalized — fairness, explainability, and compliance are automated across the lifecycle. ROI measurement is robust and standardized, with scorecards at the executive level. The organization is recognized as an industry benchmark, setting standards for AI maturity and innovation.'
}