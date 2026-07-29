"""
Pre-loaded candidate database for TalentConnect.

Real 0626-cohort candidates, classified once using the Skill Marriage method
(prior experience x new course skills -> unique value, recommended roles,
seniority). PDPA: only full name and email are kept as identifiers; DOB,
address, NRIC, gender, photo and phone are excluded by design.

This data is bundled with the app so it is always present and survives reboots.
To grow the database monthly, new cohorts are appended to CANDIDATE_DB (a future
"Add cohort" upload workflow can automate this).
"""

# Course code -> (short label, full name)
COURSES = {
    "PDDM": "Digital Marketing",
    "PDDS": "Data Science",
    "PDDI": "Digital Innovation",
    "PDFSWD": "Full Stack Web Development",
    "PDCA": "Cloud Administration",
    "ACIS": "Infrastructure Support",
}

CANDIDATE_DB = [
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Darren Tan Zhi Hao",
  "email": "darrentan.1310@gmail.com",
  "years_experience": "15+",
  "industry_background": "Presales & enterprise solutions (CX/eCommerce)",
  "prior_experience_summary": "15+ years in presales, project management and enterprise CX/eCommerce solutioning at Tech Mahindra, with an MBA and extensive SAP certifications.",
  "skills": [
   "Presales Solutioning",
   "Project Management (Scrum)",
   "eCommerce & CX Platforms",
   "SAP (S/4HANA, Commerce, CDC)",
   "Stakeholder Engagement",
   "MarTech / CDP",
   "Digital Marketing",
   "Google Ads & Facebook Marketing"
  ],
  "skill_marriage": "Combines deep enterprise CX/MarTech and presales solutioning with formal digital-marketing skills — strong fit for MarTech consulting, marketing-technology or senior digital-strategy roles bridging business and platforms.",
  "recommended_roles": [
   "MarTech / Marketing Technology Consultant",
   "Digital Marketing Strategist / Manager",
   "CX / eCommerce Solutions Consultant"
  ],
  "seniority": "Senior IC / Team-Lead potential",
  "seniority_note": "Genuinely senior with MBA, presales leadership and MarTech depth — one of the stronger profiles for a strategy/consulting-level marketing role."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Jaz Choong Fei Leng",
  "email": "notifyjcfl@gmail.com",
  "years_experience": "20+",
  "industry_background": "Administrative & operations (banking, property)",
  "prior_experience_summary": "20+ years in administrative and operational roles across UOB, Moet Hennessy and property, including a bank brand-revitalisation project and vendor coordination.",
  "skills": [
   "Administrative Operations",
   "Project Coordination",
   "Vendor & Stakeholder Management",
   "Facebook Ads & ROAS",
   "Google Analytics",
   "Marketing Automation (HubSpot, Make)",
   "Microsoft Office",
   "Basic RPA"
  ],
  "skill_marriage": "Pairs two decades of administrative and vendor-coordination discipline with new digital-marketing automation skills — suited to marketing-operations and campaign-admin roles where process reliability matters as much as creative output.",
  "recommended_roles": [
   "Marketing Operations / Campaign Coordinator",
   "Marketing Automation Assistant",
   "Digital Marketing Administrator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Long tenure is administrative rather than marketing-lead; position as a dependable marketing-ops IC entering the field."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Jerlyn Lim Hui Min (林惠敏)",
  "email": "jerlynlim7777@gmail.com",
  "years_experience": "7+",
  "industry_background": "Real estate sales & marketing",
  "prior_experience_summary": "Real estate consultant since 2019 handling HDB/private sales and leasing, using property portals and social media for marketing and lead generation.",
  "skills": [
   "Property Marketing",
   "Social Media Marketing",
   "Lead Generation",
   "Negotiation",
   "Client Advisory",
   "Market Analysis",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines hands-on property marketing and social-media lead generation with formal digital-marketing skills — a natural fit for real-estate, property-tech or lead-gen focused marketing roles.",
  "recommended_roles": [
   "Digital Marketing Executive (Real Estate / PropTech)",
   "Social Media & Lead Gen Executive",
   "Content & Campaign Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Self-employed marketing experience is practical but informal; entry-to-mid marketing roles fit well."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Joycelyn Siw Lee Foong",
  "email": "joycelyn.siw_922@yahoo.com.sg",
  "years_experience": "15+",
  "industry_background": "Automotive corporate sales & admin",
  "prior_experience_summary": "15+ years in automotive corporate sales at Goldbell and Borneo Motors, plus financial-advisory and administrative roles, with roadshow and account development experience.",
  "skills": [
   "Corporate Sales",
   "Account Acquisition & Retention",
   "Roadshow / Event Marketing",
   "Client Relationship Management",
   "Sales Proposals",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines long corporate-sales and event/roadshow experience with new digital-marketing skills — suited to field-marketing, event-marketing or sales-support marketing roles.",
  "recommended_roles": [
   "Event / Field Marketing Executive",
   "Digital Marketing Executive (B2B)",
   "Sales & Marketing Coordinator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Sales-strong; marketing is new, so entry-to-mid marketing roles fit best."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Lam Yeon Yin",
  "email": "lamyeonyin@yahoo.com.sg",
  "years_experience": "30",
  "industry_background": "Credit & accounts-receivable (finance)",
  "prior_experience_summary": "Nearly 30 years in credit management and accounts receivable at PERSOLKELLY and Samsung, including debt recovery, DSO reduction and system migration.",
  "skills": [
   "Credit & AR Management",
   "Debt Recovery",
   "Process Improvement",
   "Data Governance",
   "Stakeholder Management",
   "Excel / Reporting",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Pairs deep finance/credit-operations discipline with new digital-marketing skills — a niche fit for marketing-operations, analytics or CRM roles where numerical rigor and process control add value.",
  "recommended_roles": [
   "Marketing Operations / Analytics Executive",
   "CRM & Data Marketing Executive",
   "Digital Marketing Executive (B2B Finance)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Very senior in finance; as a marketing pivot, best positioned in data/ops-leaning marketing roles rather than creative/brand."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Linda Lim Ping Ping (Lin Binbin Linda)",
  "email": "linda_lim_pp@yahoo.com.sg",
  "years_experience": "20+",
  "industry_background": "Financial services, paraplanning & sales admin",
  "prior_experience_summary": "20+ years across banking relationship management, insurance compliance and financial-advisory paraplanning, with CRM and client-servicing depth.",
  "skills": [
   "Client Relationship Management",
   "Financial Services Admin",
   "Compliance & Risk",
   "Sales Strategy",
   "CRM Data Management",
   "Paraplanning",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines financial-services client management and compliance experience with new digital-marketing skills — suited to marketing or CRM roles in banking/insurance/wealth where trust and compliance matter.",
  "recommended_roles": [
   "Digital Marketing Executive (Financial Services)",
   "CRM / Client Marketing Executive",
   "Marketing Operations Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Extensive but admin/sales-based; marketing is new, so entry-level marketing roles in finance suit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Liu Hong De, Ranson",
  "email": "ransonliu@gmail.com",
  "years_experience": "6+",
  "industry_background": "Operations & business ownership (courier/logistics)",
  "prior_experience_summary": "Operations Director and business owner running courier and trading operations, budgeting, recruitment and social-media-driven product promotion.",
  "skills": [
   "Operations Management",
   "Supply Chain Management",
   "Budgeting & Financial Management",
   "Social Media Promotion",
   "Live Advertising",
   "Leadership",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines hands-on business-ownership and operations leadership with new digital-marketing skills — can market a business he also understands operationally, useful for SME growth or performance-marketing roles.",
  "recommended_roles": [
   "Digital Marketing Executive (SME / owner-operator context)",
   "Social Media & Performance Marketing Executive",
   "Marketing Operations Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong ownership mindset but formal marketing depth is new; entry-to-mid marketing roles fit best."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Ng Shuang Yean, Evelyn (Huang Shuangyuan)",
  "email": "evelynsyng@gmail.com",
  "years_experience": "15+",
  "industry_background": "Automotive & commercial-vehicle sales",
  "prior_experience_summary": "15+ years in automotive/commercial-vehicle sales at Goldbell and Eurokars, with a Marketing Management degree, sales reporting and presentation design.",
  "skills": [
   "B2B Sales",
   "Sales Presentation & Deck Design",
   "Client Relationship Management",
   "Sales Reporting & Forecasting",
   "Marketing Management (degree)",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Marries a marketing degree and long automotive-sales experience with refreshed digital-marketing skills — well suited to sales-marketing hybrid or product-marketing roles in automotive/industrial sectors.",
  "recommended_roles": [
   "Digital Marketing Executive (Automotive / Industrial)",
   "Product / Sales Marketing Executive",
   "Content & Campaign Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Marketing degree plus sales gives a fair marketing foundation; mid-level marketing roles are realistic."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Quak Kim Hiang, Jensen (Guo Jinxian)",
  "email": "quakkh@hotmail.com",
  "years_experience": "20+",
  "industry_background": "Regional sales & operations (security, aerospace)",
  "prior_experience_summary": "20+ years across aerospace, security-solutions and property sales, including SEA regional sales management, partner development and product demos.",
  "skills": [
   "B2B Regional Sales",
   "Partner & Channel Development",
   "Sales & Marketing Planning",
   "Product Demonstration",
   "Stakeholder Management",
   "Digital Marketing (foundational)",
   "CRM"
  ],
  "skill_marriage": "Marries long B2B regional-sales and partner-development experience with new digital-marketing skills — well suited to sales-marketing hybrid roles that generate and nurture leads across SEA channels.",
  "recommended_roles": [
   "Sales & Marketing Executive (B2B)",
   "Channel / Partner Marketing Executive",
   "Lead Generation / Demand Gen Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior in sales; digital-marketing execution is new, so pitch at senior-sales-with-marketing rather than marketing-lead."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Sandria Wang Yueling",
  "email": "moonbell@gmail.com",
  "years_experience": "10+",
  "industry_background": "Insurance & healthcare claims administration",
  "prior_experience_summary": "10+ years in insurance/healthcare claims and underwriting support at Great Eastern and CPF Board, with compliance and stakeholder coordination.",
  "skills": [
   "Claims Processing",
   "Regulatory Compliance",
   "Stakeholder Management",
   "Data Entry & Accuracy",
   "Microsoft Excel",
   "Digital Marketing (foundational)",
   "Content Basics"
  ],
  "skill_marriage": "Combines regulated-industry claims/compliance rigor with new digital-marketing skills — a fit for marketing roles in insurance, healthcare or finance where compliance-aware content and accuracy are valued.",
  "recommended_roles": [
   "Digital Marketing Executive (Insurance / Healthcare)",
   "Marketing Compliance / Content Coordinator",
   "CRM & Marketing Ops Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Domain-strong but marketing is a fresh pivot; entry-level marketing roles in regulated sectors suit best."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Teng Ngee Heng, Richard (Ding Yixing, Richard)",
  "email": "Tngeeheng@live.com.sg",
  "years_experience": "15+",
  "industry_background": "Technical B2B sales & marketing (engineering/semicon)",
  "prior_experience_summary": "15+ years in technical B2B sales and marketing across engineering and semiconductor suppliers, managing key accounts and product awareness campaigns.",
  "skills": [
   "Technical B2B Sales",
   "Key Account Management",
   "Marketing & Roadshow Execution",
   "Supply Chain Coordination",
   "Customer Relationship Management",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Pairs long technical-sales and account-management experience with new digital-marketing skills — suited to B2B/industrial marketing where product knowledge and customer insight drive campaigns.",
  "recommended_roles": [
   "B2B / Industrial Marketing Executive",
   "Account-Based Marketing Executive",
   "Digital Marketing Executive (Technical products)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Solid sales track record; marketing execution is new, so mid-level B2B marketing roles fit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Wilson Ng Hock Leong",
  "email": "wilsonng@honghill.sg",
  "years_experience": "20+",
  "industry_background": "Operations management & property sales",
  "prior_experience_summary": "Operations Manager since 2016 plus 30 years as a property agent, running online and social-media advertising for lead generation.",
  "skills": [
   "Operations Management",
   "Property Sales & Rentals",
   "Online & Social Media Advertising",
   "Lead Generation",
   "Team Management",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Pairs operations leadership and long self-driven property advertising experience with formal digital-marketing skills — fits SME marketing or real-estate lead-generation roles.",
  "recommended_roles": [
   "Digital Marketing Executive (Real Estate / SME)",
   "Social Media & Lead Gen Executive",
   "Marketing Operations Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Brief CV; marketing experience is informal/self-driven, so entry-level marketing roles suit best."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Cheng Kiat Nian, Tidus (Zeng Jinian)",
  "email": "Chengtidus@gmail.com",
  "years_experience": "10+",
  "industry_background": "EHS / workplace safety & security (enforcement)",
  "prior_experience_summary": "5+ years in EHS/safety plus years as a Special Duty Officer in the Ministry of Home Affairs, holding multiple safety and security registrations.",
  "skills": [
   "Workplace Safety & Health",
   "Risk Assessment",
   "Surveillance & Investigation",
   "Compliance",
   "Data Analysis (foundational)",
   "Power BI (foundational)",
   "Python (foundational)"
  ],
  "skill_marriage": "Pairs safety/security enforcement and risk-assessment experience with new data-science skills — a niche fit for safety analytics, compliance data or risk-monitoring analyst roles.",
  "recommended_roles": [
   "Safety / Risk Data Analyst",
   "Compliance Analyst",
   "Data Analyst (EHS / Operations)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Domain is safety/security, not analytical; data science is a significant pivot, so entry-level analyst roles suit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Chris Ng Yu Yee (Huang Youyi)",
  "email": "birthchris@hotmail.com",
  "years_experience": "10+",
  "industry_background": "Civil/structural engineering & project management (public sector)",
  "prior_experience_summary": "Engineer at HDB and PUB managing contractors, project timelines, contract/enforcement and reporting in civil & structural engineering.",
  "skills": [
   "Project Management",
   "Contract Management",
   "Data Analysis",
   "Power BI",
   "Python (foundational)",
   "Stakeholder Management",
   "Reporting",
   "Machine Learning (foundational)"
  ],
  "skill_marriage": "Combines public-sector engineering project management with new data-science skills — suited to data-analyst or project-analytics roles in construction, facilities, utilities or govtech where domain plus analytics is valued.",
  "recommended_roles": [
   "Data Analyst (Engineering / Public Sector)",
   "Project / Operations Analyst",
   "BI Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Solid engineering experience; data science is new, so entry-to-mid analyst roles with domain context fit best."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Goh Siew Choo",
  "email": "gohjuvelia@gmail.com",
  "years_experience": "20+",
  "industry_background": "Sales operations & procurement (electronics)",
  "prior_experience_summary": "20+ years in sales coordination, procurement and operations at Panasonic, handling large sales-data volumes and reporting across SAP, Oracle and Salesforce.",
  "skills": [
   "Sales Data Handling & Reporting",
   "Enterprise Systems (SAP, Oracle, Salesforce)",
   "Advanced Excel",
   "Order Tracking",
   "Data Validation",
   "Data Analytics (foundational)"
  ],
  "skill_marriage": "Combines two decades of sales-data and enterprise-systems experience with new data-analytics skills — suited to business/sales-analyst roles where familiarity with SAP/Oracle/Salesforce data is an asset.",
  "recommended_roles": [
   "Business / Sales Data Analyst",
   "Reporting Analyst",
   "Junior Data Analyst (Operations)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong data-handling exposure but analytics is new; entry-to-mid analyst roles with enterprise-systems context fit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Joyce Tan Poh Lee",
  "email": "jtan704@gmail.com",
  "years_experience": "16+",
  "industry_background": "Human resources (multi-industry)",
  "prior_experience_summary": "16+ years as HR professional/lead partner across IT, healthcare, aerospace and manufacturing, building HR frameworks and managing HRIS/employee data.",
  "skills": [
   "HR Operations",
   "HRIS & Employee Data Management",
   "Recruitment & Workforce Planning",
   "HR Analytics (foundational)",
   "Data Analysis (foundational)",
   "Power BI (foundational)"
  ],
  "skill_marriage": "Combines deep HR-operations and HRIS-data experience with new data-science skills — a strong fit for people-analytics / HR-data-analyst roles where HR-domain understanding is essential.",
  "recommended_roles": [
   "People / HR Analytics Analyst",
   "HR Data Analyst",
   "Business Analyst (HR)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior HR practitioner; as a data pivot, people-analytics is the natural bridge role at senior-IC level."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Liew Wai San",
  "email": "liz84liew@yahoo.com",
  "years_experience": "10+",
  "industry_background": "Business intelligence & data engineering (banking)",
  "prior_experience_summary": "A decade of BI/data-analyst and data-engineering experience in MNCs and banking (Bank of Singapore), with SQL, SSIS, Power BI, Tableau, Snowflake and Python.",
  "skills": [
   "SQL / T-SQL",
   "SSIS / ETL",
   "Power BI",
   "Tableau",
   "Snowflake",
   "Python (Pandas, NumPy)",
   "Data Warehousing",
   "Machine Learning (foundational)"
  ],
  "skill_marriage": "Already a genuine BI/data-engineering professional now formalising data-science skills — one of the strongest technical DS profiles, ready for data-analyst, BI or junior data-scientist roles with real production experience.",
  "recommended_roles": [
   "Data Analyst / BI Analyst",
   "Data Engineer",
   "Junior Data Scientist"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Strong existing technical depth (SQL, ETL, BI); genuinely job-ready for mid-senior data roles."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Lua Lan Yan, Lynn",
  "email": "lynnlualy@gmail.com",
  "years_experience": "15+",
  "industry_background": "Human resources & real estate",
  "prior_experience_summary": "15+ years across HR (recruitment, HRBP, payroll, HR metrics via Workday/Excel) and real estate, most recently Senior HR Executive at MX Caterers.",
  "skills": [
   "HR Analytics & Metrics",
   "HRIS (Workday)",
   "Recruitment",
   "Excel Reporting",
   "Data Analysis (foundational)",
   "Stakeholder Management"
  ],
  "skill_marriage": "Combines HR-business-partnering and HR-metrics experience with new data-science skills — suited to people-analytics or HR-reporting analyst roles that turn workforce data into insight.",
  "recommended_roles": [
   "People / HR Analytics Analyst",
   "HR Data / Reporting Analyst",
   "Business Analyst (HR)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "HR-metrics exposure gives a head start; data science is new, so mid-level people-analytics roles fit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Madhuri Sunder Khubchandani",
  "email": "madu72@yahoo.com",
  "years_experience": "17+",
  "industry_background": "Service operations management (visa/airline)",
  "prior_experience_summary": "17+ years in service operations and team management at VFS and airlines, leading teams of 10-12, process improvement and client liaison with government officials.",
  "skills": [
   "Operations Management",
   "Team Leadership",
   "Process Improvement",
   "Customer Relationship Management",
   "Data Analysis (foundational)",
   "Power BI (foundational)",
   "Reporting"
  ],
  "skill_marriage": "Combines long service-operations leadership with new data-science skills — suited to operations-analytics or business-analyst roles where understanding service processes strengthens the analysis.",
  "recommended_roles": [
   "Operations / Business Analyst",
   "Data Analyst (Service Operations)",
   "Process & Performance Analyst"
  ],
  "seniority": "Senior IC / Team-Lead potential",
  "seniority_note": "Senior in operations management; as a data pivot, pitch analytics roles at senior-IC with an operations-leadership angle."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Sarah Lim Chui Shing",
  "email": "sarah_0566@hotmail.com",
  "years_experience": "10+",
  "industry_background": "Commercial finance & FP&A (electronics/APAC)",
  "prior_experience_summary": "Assistant Manager at Sony leading demand planning, FP&A, forecasting and reporting automation across 6 SEA markets for 10+ years.",
  "skills": [
   "FP&A & Forecasting",
   "Demand Planning",
   "SAP BW / S4 HANA",
   "RPA (Automation Anywhere)",
   "Power BI",
   "Python",
   "Data Visualisation",
   "Stakeholder Management"
  ],
  "skill_marriage": "Combines 10+ years of commercial-finance and demand-planning ownership with new data-science skills — can build forecasting models and analytics dashboards grounded in real FP&A and sales-planning logic.",
  "recommended_roles": [
   "Finance Data Analyst / FP&A Analyst",
   "Business Intelligence Analyst (Commercial)",
   "Analytics Translator / Planning Analyst"
  ],
  "seniority": "Senior IC / Team-Lead potential",
  "seniority_note": "Strong senior evidence; as a data-science pivot, pitch analytics roles at senior-IC rather than data-lead titles."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Subramanian Chitra",
  "email": "",
  "years_experience": "15+",
  "industry_background": "IT project management (govt, banking, logistics)",
  "prior_experience_summary": "Senior Project Manager with 15+ years delivering large technology programs at GovTech and banking, including AWS cloud migration, data platforms and IM8 compliance.",
  "skills": [
   "Project & Program Management",
   "Cloud Delivery (AWS)",
   "Enterprise Data Platforms",
   "Stakeholder Governance",
   "Risk & Quality Control",
   "Digital Transformation",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines senior IT-program management and enterprise-data-platform delivery with new data-science skills — suited to data-project-management, analytics-delivery or business-analyst roles bridging tech and data teams.",
  "recommended_roles": [
   "Data / Analytics Project Manager",
   "Business Analyst (Data Platforms)",
   "Data Product / Delivery Lead"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Genuinely senior PM; best positioned leading data/analytics delivery rather than hands-on data-scientist roles."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Teh Chun Cheong",
  "email": "chuncheongteh@gmail.com",
  "years_experience": "10+",
  "industry_background": "Manufacturing & technical operations (QA/food)",
  "prior_experience_summary": "Manufacturing and technical roles across sensor maintenance, lab manufacturing and food safety, with ISO auditing certifications and self-taught Python/web courses.",
  "skills": [
   "Manufacturing Operations",
   "Quality / ISO Auditing",
   "Python (self-taught)",
   "Data & Digital Analytics (foundational)",
   "Web Development Basics",
   "Process Compliance"
  ],
  "skill_marriage": "Combines hands-on manufacturing/QA and ISO-auditing experience with newly acquired Python and data-analytics skills — a fit for manufacturing analytics, quality-data or process-monitoring analyst roles.",
  "recommended_roles": [
   "Data Analyst (Manufacturing / QA)",
   "Quality / Process Data Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Entry",
  "seniority_note": "Technical-operations background with self-taught coding; genuine analytics experience is limited, so entry-level roles fit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Akbar Yaseen S/O Mohamad Jeenah",
  "email": "akbaryaseen56@gmail.com",
  "years_experience": "18+",
  "industry_background": "Business operations & administrative coordination",
  "prior_experience_summary": "18+ years in business operations, dispatch/logistics coordination, documentation and government liaison, now pivoting to digital innovation and technology.",
  "skills": [
   "Business Process Coordination",
   "Documentation & Compliance",
   "Logistics Coordination",
   "Government Liaison",
   "Microsoft Office",
   "Digital Innovation Tools (foundational)",
   "Reporting"
  ],
  "skill_marriage": "Combines long operations/administration experience with new digital-innovation skills — suited to business-process-automation or operations-digitalisation support roles where process knowledge guides the tooling.",
  "recommended_roles": [
   "Business Process / Operations Analyst",
   "Process Automation Executive",
   "Digital Transformation Support Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Operations-strong but digital skills are new; entry-to-mid transformation-support roles fit best."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Chia Zi Yang (Xie Ziyang)",
  "email": "chiaziyang@hotmail.com",
  "years_experience": "8+",
  "industry_background": "Banking & wealth advisory",
  "prior_experience_summary": "Wealth advisor and relationship manager at Standard Chartered and UOB, award-winning in investment/wealth sales and client-portfolio management.",
  "skills": [
   "Wealth & Relationship Management",
   "Investment & Financial Planning",
   "Client Portfolio Management",
   "New Business Generation",
   "Digital Innovation Tools (foundational)",
   "Data Analysis (foundational)"
  ],
  "skill_marriage": "Combines banking/wealth-advisory experience with new digital-innovation skills — suited to fintech, digital-banking-transformation or client-experience-innovation roles in financial services.",
  "recommended_roles": [
   "Digital Transformation / Innovation Analyst (Financial Services)",
   "Business Analyst (Wealth / Fintech)",
   "Client Experience / Digital Product Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong wealth-sales record; digital-innovation is new, so mid-level fintech/BA roles fit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Choong Joo Ling (Zhuang Rulin)",
  "email": "idcc318@gmail.com",
  "years_experience": "15+",
  "industry_background": "Grants administration & insurance claims (academic/public)",
  "prior_experience_summary": "Grant management and administration across NUS, NTU and government, plus insurance claims experience, with a Maths degree, Psychology honours and SPSS/data-analysis skills.",
  "skills": [
   "Grant & Programme Administration",
   "Qualitative Data Analysis (SPSS)",
   "Digital Media Design (Photoshop, Canva)",
   "Process Management",
   "Digital Innovation Tools (foundational)",
   "Content Creation"
  ],
  "skill_marriage": "Combines administration, research-data-analysis (SPSS) and design skills with new digital-innovation tools — suited to digital-content, programme-digitalisation or research/data-support roles in academic or public-sector settings.",
  "recommended_roles": [
   "Digital Content / Media Executive",
   "Programme / Business Analyst (Public Sector)",
   "Data Support / Research Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Varied admin and analytical background; digital-innovation is new, so mid-level roles fit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Gary Chan Yue Min",
  "email": "garychan0198@hotmail.com",
  "years_experience": "10+",
  "industry_background": "HR / talent acquisition (tech, e-commerce)",
  "prior_experience_summary": "10+ years in talent acquisition and HR leadership across e-commerce and software firms, leading regional TA teams and data-driven sourcing strategies.",
  "skills": [
   "Talent Acquisition",
   "Employer Branding",
   "Talent Pipeline & Market Analysis",
   "Team Leadership",
   "Digital Innovation Tools (foundational)",
   "Process Automation (foundational)"
  ],
  "skill_marriage": "Combines TA leadership and data-driven-sourcing experience with new digital-innovation skills — suited to HR-tech, recruitment-automation or talent-analytics roles that modernise hiring processes.",
  "recommended_roles": [
   "HR-Tech / Recruitment Automation Analyst",
   "Talent Analytics / Ops Analyst",
   "Business Analyst (People)"
  ],
  "seniority": "Senior IC / Team-Lead potential",
  "seniority_note": "Led regional TA teams; strong domain, digital-innovation skills fresh — pitch HR-tech/analytics at senior-IC."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Iris Low Mui Hoon (Liu Meiyun)",
  "email": "donirislow@gmail.com",
  "years_experience": "10+",
  "industry_background": "Supply chain & franchise management",
  "prior_experience_summary": "Supply-chain professional in supply planning, demand forecasting and procurement, plus franchise management, with prior Lithan data-visualisation training and Power BI/Python/Azure skills.",
  "skills": [
   "Supply Chain & Demand Planning",
   "Procurement",
   "Power BI",
   "Python",
   "Microsoft Azure",
   "Data Visualisation",
   "Digital Innovation Tools"
  ],
  "skill_marriage": "Combines supply-chain planning and forecasting with prior data-visualisation training and new digital-innovation skills — well suited to supply-chain-analytics or operations-digitalisation roles blending domain and tools.",
  "recommended_roles": [
   "Supply Chain / Operations Analyst",
   "Business Analyst (Digital Transformation)",
   "Data Visualisation / BI Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Prior data-viz training gives an edge; mid-level analytics/transformation roles in supply chain fit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Lee Hock Peng (Li FuPing)",
  "email": "hockpengl1@gmail.com",
  "years_experience": "25+",
  "industry_background": "Manufacturing operations (automation systems)",
  "prior_experience_summary": "Director of Manufacturing at Nutek for 25+ years, leading manufacturing and procurement teams of 70, production optimisation and automated-systems delivery.",
  "skills": [
   "Manufacturing Operations Management",
   "Production Optimisation",
   "Team Leadership (70 staff)",
   "Capacity Planning",
   "Vendor Management",
   "Digital Innovation Tools (foundational)",
   "Automation"
  ],
  "skill_marriage": "Combines senior manufacturing-operations leadership and automated-systems experience with new digital-innovation skills — suited to manufacturing-digitalisation, Industry-4.0 or operations-transformation roles.",
  "recommended_roles": [
   "Manufacturing Digital Transformation Lead",
   "Operations / Process Innovation Analyst",
   "Industry 4.0 / Automation Consultant"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Very senior operations leader; best positioned in transformation-lead roles leveraging manufacturing depth."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Nadia Binte Idris",
  "email": "naya667@hotmail.com",
  "years_experience": "10+",
  "industry_background": "Human resources & talent acquisition (shared services)",
  "prior_experience_summary": "HR/TA professional across government shared services and PayPal, skilled in HR function setup, ATS/HRIS platforms (Workday, Greenhouse, iCIMS) and compliance.",
  "skills": [
   "HR Function Setup",
   "ATS/HRIS (Workday, Greenhouse, iCIMS)",
   "Recruitment & Workforce Planning",
   "Process Improvement",
   "Digital Innovation Tools (foundational)",
   "Power Automate (foundational)"
  ],
  "skill_marriage": "Combines HR-systems and process-transformation experience with new digital-innovation skills — suited to HR-tech, digital-HR-transformation or business-analyst roles improving people processes with automation.",
  "recommended_roles": [
   "HR Digital Transformation / HR-Tech Analyst",
   "Business Analyst (People Systems)",
   "Process Automation Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong HR-systems exposure; digital-innovation skills are new, so mid-level HR-tech/BA roles fit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Ng Joon Hui (Huang Joon Hui)",
  "email": "",
  "years_experience": "20",
  "industry_background": "Procurement & engineering (marine, port, corporate)",
  "prior_experience_summary": "20 years spanning marine engineering, port operations and corporate procurement, specialising in strategic sourcing, contract management and data-driven decisions.",
  "skills": [
   "Strategic Sourcing & Procurement",
   "Contract Management",
   "Vendor Management",
   "Data-Driven Decision Making",
   "Logistics & Warehouse Ops",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines long procurement/engineering and data-driven-sourcing experience with new digital-innovation skills — suited to procurement-digitalisation, supply-chain-analytics or business-process-transformation roles.",
  "recommended_roles": [
   "Procurement / Supply Chain Digital Transformation Analyst",
   "Business Process / Operations Analyst",
   "Business Analyst (Sourcing)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior in procurement/engineering; digital-innovation is new, so pitch transformation/BA roles at senior-IC with domain depth."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Raja",
  "email": "rjpm2403@gmail.com",
  "years_experience": "9",
  "industry_background": "Data centre operations & field engineering",
  "prior_experience_summary": "9 years in data-centre technician and field-engineer roles at Microsoft, Equinix and Rubicor, handling servers, networking, diagnostics and migration projects.",
  "skills": [
   "Data Centre Operations",
   "Hardware Troubleshooting",
   "Networking",
   "SLA/Ticketing Workflows",
   "Digital Innovation Tools (foundational)",
   "Power Automate (foundational)",
   "Process Documentation"
  ],
  "skill_marriage": "Combines hands-on data-centre/infrastructure experience with new digital-innovation skills — suited to IT operations automation, digital-workflow or infrastructure-transformation support roles.",
  "recommended_roles": [
   "IT Operations / Automation Executive",
   "Digital Workflow / Process Analyst",
   "Infrastructure Support (Digital Transformation)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Solid infrastructure IC; digital-innovation/low-code is new, so entry-to-mid transformation-support roles fit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Tan Sheng Rong Leonard (Chen Shengrong Leonard)",
  "email": "",
  "years_experience": "20+",
  "industry_background": "Banking & wealth management (leadership)",
  "prior_experience_summary": "20+ years in consumer/priority/private banking and wealth management, leading multi-tiered advisory teams and championing digital transformation at DBS.",
  "skills": [
   "Wealth & Relationship Management",
   "Sales Leadership",
   "Digital Transformation",
   "Compliance & Sales Governance",
   "Social/Digital Marketing",
   "Process Innovation",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines senior banking/wealth leadership and prior digital-transformation advocacy with new digital-innovation skills — suited to digital-transformation, fintech-business or innovation-lead roles in financial services.",
  "recommended_roles": [
   "Digital Transformation Consultant (Financial Services)",
   "Business / Innovation Analyst",
   "Digital Project Manager"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Genuinely senior banking leader; best positioned in transformation/consulting roles rather than hands-on tool building."
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Tay Shijia",
  "email": "tay_shijia@hotmail.com",
  "years_experience": "15+",
  "industry_background": "IT project management & data translation (govt, banking)",
  "prior_experience_summary": "Project Manager and Data Translator at GovTech (MOH) and DBS, owning product backlogs, Agile delivery and turning business needs into data products and dashboards.",
  "skills": [
   "Agile Product / Project Management",
   "Data Translation & Requirements",
   "Dashboards & Analytics Delivery",
   "Stakeholder Management",
   "Scrum (PSM, PSPO)",
   "Digital Innovation Tools",
   "Digital Transformation"
  ],
  "skill_marriage": "Combines Agile product/project management and data-translation experience with new digital-innovation skills — a strong fit for digital-product, business-analyst or transformation-delivery roles bridging business and tech.",
  "recommended_roles": [
   "Digital Product Owner / Business Analyst",
   "Digital Transformation Project Manager",
   "Data Product / Delivery Analyst"
  ],
  "seniority": "Senior IC / Team-Lead potential",
  "seniority_note": "Strong Agile/product and data-translation background; genuinely ready for senior BA/product roles."
 },
 {
  "specialist": "Jim",
  "course_code": "PDFSWD",
  "course_name": "Professional Diploma in Full Stack Web Development",
  "cohort": "WD-0626",
  "full_name": "Govindan Sathiya",
  "email": "govindan_sathya@yahoo.com",
  "years_experience": "5+",
  "industry_background": "IT infrastructure & cloud administration",
  "prior_experience_summary": "5+ years in Windows Server administration, hybrid-cloud (AWS, M365) and IT security operations across enterprise and government projects, now adding web development.",
  "skills": [
   "Windows Server & Active Directory",
   "Cloud Infrastructure (AWS, M365)",
   "IT Security Operations",
   "Virtualisation",
   "Web Development (learning)",
   "IIS / Databases"
  ],
  "skill_marriage": "Combines solid IT-infrastructure and cloud-admin experience with new full-stack web-development skills — well positioned for DevOps, cloud-app-development or full-stack roles with strong infra grounding.",
  "recommended_roles": [
   "Full Stack Developer (Cloud/Infra background)",
   "DevOps / Cloud Engineer",
   "Application Support / Developer"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Real infra depth plus new dev skills; junior-to-mid developer or DevOps roles are a genuine fit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDFSWD",
  "course_name": "Professional Diploma in Full Stack Web Development",
  "cohort": "WD-0626",
  "full_name": "Katherine Fiedalan Nayan",
  "email": "karenayan@gmail.com",
  "years_experience": "15+",
  "industry_background": "PCB design & hardware R&D engineering",
  "prior_experience_summary": "R&D/PCB layout design engineer at Agilent for years, expert in Mentor Graphics, Altium, SAP and CAD tools, with project management and QC background.",
  "skills": [
   "PCB / Hardware Design",
   "CAD Tools (Mentor, Altium, Cadence)",
   "SAP (PP/MM)",
   "Project Management",
   "Web Development (foundational)",
   "Problem Solving"
  ],
  "skill_marriage": "Combines deep hardware/PCB-design engineering with new web-development skills — suited to technical roles bridging hardware and software, EDA tooling, or engineering-application development.",
  "recommended_roles": [
   "Application Developer (Engineering / Hardware domain)",
   "Technical / Software Support Engineer",
   "Full Stack Developer (Junior)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong hardware engineer; software dev is new, so junior-developer or hardware-software bridge roles fit."
 },
 {
  "specialist": "Jim",
  "course_code": "PDFSWD",
  "course_name": "Professional Diploma in Full Stack Web Development",
  "cohort": "WD-0626",
  "full_name": "Siti Shufiah Binte Ali Bagusher",
  "email": "shufiah@quicksender.net",
  "years_experience": "13+",
  "industry_background": "eCommerce, sales & social media marketing",
  "prior_experience_summary": "13+ years in eCommerce management, sales and social-media marketing, growing follower bases and mailing lists, plus event planning, with a biomedical-informatics diploma.",
  "skills": [
   "eCommerce Management",
   "Social Media Marketing",
   "Sales & Marketing",
   "Content & Community Growth",
   "Web Development (foundational)",
   "Customer Database Management"
  ],
  "skill_marriage": "Combines eCommerce and social-media-marketing experience with new web-development skills — suited to eCommerce-web, front-end or web-content-management roles blending commerce and code.",
  "recommended_roles": [
   "Front-End / Web Developer (eCommerce)",
   "eCommerce Web Executive",
   "Web Content / CMS Developer"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Commerce-strong; dev is new, so junior web-developer roles with an eCommerce angle fit best."
 },
 {
  "specialist": "Jim",
  "course_code": "PDFSWD",
  "course_name": "Professional Diploma in Full Stack Web Development",
  "cohort": "WD-0626",
  "full_name": "William Chin Wei Lian",
  "email": "",
  "years_experience": "20+",
  "industry_background": "Engineering & manufacturing operations",
  "prior_experience_summary": "20+ years in manufacturing, quality and engineering management at Emerson, leading automation/digitalisation and product-transfer projects, with a Mechanical Engineering degree.",
  "skills": [
   "Engineering & Operations Management",
   "Process Automation & Digitalisation",
   "Project Management",
   "Quality Management",
   "Web Development (foundational)",
   "Cross-functional Leadership"
  ],
  "skill_marriage": "Combines senior engineering-operations and digital-transformation leadership with new web-development skills — suited to technical-project, engineering-software or digitalisation roles rather than pure coding.",
  "recommended_roles": [
   "Technical Project Manager (Engineering Software)",
   "Digital Transformation / Automation Analyst",
   "Application / Solutions Analyst"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Very senior in operations; web-dev is a fresh add-on, so leverage it in a technical-leadership/transformation role, not junior developer."
 },
 {
  "specialist": "Jim",
  "course_code": "ACIS",
  "course_name": "Advanced Certificate in Infrastructure Support",
  "cohort": "EIT-0626",
  "full_name": "Choo Wee Long (Zhu Weilong)",
  "email": "weelong83@hotmail.com",
  "years_experience": "23",
  "industry_background": "Aerospace / avionics engineering (RSAF)",
  "prior_experience_summary": "23+ years as an RSAF avionics engineer and certified technical trainer, leading a team of 12, maintenance standards auditing and F-15 systems training.",
  "skills": [
   "Avionics / Systems Engineering",
   "Technical Training",
   "Maintenance Standards Auditing",
   "Team Leadership",
   "IT Infrastructure Support (learning)",
   "Analytical Thinking"
  ],
  "skill_marriage": "Combines deep engineering, auditing and technical-training experience with new infrastructure-support skills — suited to IT infrastructure, technical-training or systems-support roles that value engineering discipline.",
  "recommended_roles": [
   "Infrastructure Support Engineer",
   "IT Systems / Technical Support",
   "Technical Trainer (IT)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior engineer with strong discipline; IT infra is new, so pitch mid-level infra/support with an engineering-leadership angle."
 },
 {
  "specialist": "Jim",
  "course_code": "ACIS",
  "course_name": "Advanced Certificate in Infrastructure Support",
  "cohort": "EIT-0626",
  "full_name": "Heo Swee Tong (Ye Ruizhong)",
  "email": "heojac@hotmail.com",
  "years_experience": "20+",
  "industry_background": "Corporate travel & business operations",
  "prior_experience_summary": "20+ years in corporate travel management, reservations (Amadeus) and business operations, handling corporate accounts and client servicing.",
  "skills": [
   "Corporate Travel Operations",
   "Reservation Systems (Amadeus)",
   "Customer Service",
   "Business Development",
   "IT Infrastructure Support (learning)",
   "Coordination"
  ],
  "skill_marriage": "Combines long operations/customer-service experience with new infrastructure-support skills — suited to IT service-desk or support-coordination roles leveraging strong client-handling ability.",
  "recommended_roles": [
   "IT Service Desk / Helpdesk Support",
   "IT Support Coordinator",
   "Desktop Support Executive"
  ],
  "seniority": "Entry",
  "seniority_note": "No prior IT role; infra skills are new, so entry-level support roles with training fit best."
 },
 {
  "specialist": "Jim",
  "course_code": "ACIS",
  "course_name": "Advanced Certificate in Infrastructure Support",
  "cohort": "EIT-0626",
  "full_name": "Ng Xi Jie, Jay",
  "email": "Jay.ngxj91@gmail.com",
  "years_experience": "7",
  "industry_background": "Customer service & operations administration",
  "prior_experience_summary": "7 years in customer service and operations/logistics admin across F&B and construction, handling orders, data extraction (Excel), route planning and stocktaking.",
  "skills": [
   "Customer Service",
   "Operations & Logistics Admin",
   "Data Extraction (Excel)",
   "Route Planning",
   "IT Infrastructure Support (learning)",
   "Problem Solving"
  ],
  "skill_marriage": "Combines operations/customer-service experience with new infrastructure-support skills — suited to IT service-desk or helpdesk-support roles where customer-service strength is a real asset.",
  "recommended_roles": [
   "IT Service Desk / Helpdesk Support",
   "Desktop Support Executive",
   "IT Support Executive (Junior)"
  ],
  "seniority": "Entry",
  "seniority_note": "No prior IT role; infra skills are new, so entry-level service-desk/support roles fit best."
 },
 {
  "specialist": "Jim",
  "course_code": "ACIS",
  "course_name": "Advanced Certificate in Infrastructure Support",
  "cohort": "EIT-0626",
  "full_name": "Ong Kwee Hock",
  "email": "doggies0990@gmail.com",
  "years_experience": "37+",
  "industry_background": "Aircraft systems & maintenance engineering (RSAF)",
  "prior_experience_summary": "37+ years as an RSAF aircraft systems & maintenance engineer, expert in troubleshooting, root-cause analysis, project management and engineer training.",
  "skills": [
   "Systems Maintenance & Troubleshooting",
   "Root Cause Analysis (FMEA, 5 Whys)",
   "Project & Stakeholder Management",
   "Technical Training",
   "IT Infrastructure Support (learning)",
   "Team Leadership"
  ],
  "skill_marriage": "Combines decades of systems-troubleshooting and technical-training experience with new infrastructure-support skills — suited to IT infrastructure-support or technical roles that reward strong diagnostic discipline.",
  "recommended_roles": [
   "Infrastructure Support Engineer",
   "IT Technical Support",
   "Technical Trainer (IT)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Extremely experienced engineer but IT-domain is new; pitch mid-level infra-support leveraging troubleshooting depth."
 },
 {
  "specialist": "Jim",
  "course_code": "ACIS",
  "course_name": "Advanced Certificate in Infrastructure Support",
  "cohort": "EIT-0626",
  "full_name": "Peh Kah Jun, Kane",
  "email": "kanepeh@gmail.com",
  "years_experience": "10+",
  "industry_background": "Freelance services & customer relationships",
  "prior_experience_summary": "10+ years managing freelance pet-grooming services and, recently, PHV driving, handling scheduling, client communication and payments independently.",
  "skills": [
   "Customer Service",
   "Client Relationship Management",
   "Scheduling",
   "Self-management",
   "IT Infrastructure Support (learning)"
  ],
  "skill_marriage": "Combines self-driven customer-service experience with new infrastructure-support skills — a career-changer suited to entry-level IT service-desk or support roles where reliability and customer handling matter.",
  "recommended_roles": [
   "IT Service Desk / Helpdesk Support (Junior)",
   "Desktop Support Executive (Junior)",
   "IT Support Trainee"
  ],
  "seniority": "Entry",
  "seniority_note": "Significant career change with no IT background; entry-level support roles with training suit best."
 },
 {
  "specialist": "Jim",
  "course_code": "ACIS",
  "course_name": "Advanced Certificate in Infrastructure Support",
  "cohort": "EIT-0626",
  "full_name": "Visvalingam S/O Chidambaram",
  "email": "Visvalingam2208@gmail.com",
  "years_experience": "15+",
  "industry_background": "Security operations & aircraft engineering support",
  "prior_experience_summary": "Security supervisor across commercial buildings plus earlier aircraft quality-technician experience at GE Aviation (inspections, NDT, electrical troubleshooting).",
  "skills": [
   "Security Operations",
   "Aircraft Quality Inspection / NDT",
   "Electrical Troubleshooting",
   "Incident Management",
   "IT Infrastructure Support (learning)",
   "Team Leadership"
  ],
  "skill_marriage": "Combines technical inspection/troubleshooting and security-operations experience with new infrastructure-support skills — suited to IT infrastructure, physical-IT-security or technical-support roles.",
  "recommended_roles": [
   "Infrastructure Support Engineer (Junior)",
   "IT / Security Support Executive",
   "Desktop / Technical Support"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Technical troubleshooting background helps, but IT-domain is new; entry-to-mid support roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Eng Zhi Li",
  "email": "engzhili@gmail.com",
  "years_experience": "13+",
  "industry_background": "ISOTANK logistics & commercial management",
  "prior_experience_summary": "Commercial Manager at Bulkhaul for 13+ years leading regional ISOTANK logistics accounts across SEA and China, driving pricing, tenders and vendor negotiations.",
  "skills": [
   "Commercial / Account Management",
   "Logistics & Freight Operations",
   "Contract & Tender Negotiation",
   "Power BI",
   "Power Automate",
   "Generative AI / Copilot",
   "Cross-Border Coordination"
  ],
  "skill_marriage": "Combines regional commercial/logistics account leadership with new digital-marketing and automation skills — suited to B2B marketing, logistics-marketing or commercial-digitalisation roles in the freight/supply-chain sector.",
  "recommended_roles": [
   "B2B / Commercial Marketing Executive (Logistics)",
   "Marketing & Business Development Executive",
   "Marketing Operations Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior in commercial/logistics; marketing is new. Note: CV states a Digital Innovation diploma though filed under DM — confirm course."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Ho Pei Ru, Daphne",
  "email": "",
  "years_experience": "10+",
  "industry_background": "B2B sales & account/business development",
  "prior_experience_summary": "Key Account and Business Development Manager across Bufab, Vallen and HPB, driving revenue growth, B2B webshop implementation and account analytics.",
  "skills": [
   "B2B Sales & Account Management",
   "Business Development",
   "Client Relationship Management",
   "B2B eCommerce / Webshop",
   "Data Analysis",
   "Digital Marketing (foundational)",
   "Negotiation"
  ],
  "skill_marriage": "Combines B2B sales/account-management and eCommerce experience with new digital-marketing skills — suited to B2B marketing, account-based marketing or eCommerce-marketing roles.",
  "recommended_roles": [
   "B2B / Account-Based Marketing Executive",
   "eCommerce Marketing Executive",
   "Business Development & Marketing Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong B2B sales; marketing is a fresh pivot, so mid-level B2B marketing roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Jacee Tan Boon Huay",
  "email": "jac_jae@hotmail.com",
  "years_experience": "20+",
  "industry_background": "Corporate travel management",
  "prior_experience_summary": "20+ years as Senior Travel Consultant at American Express, handling corporate travel, crisis management, GDS systems and mentoring junior consultants.",
  "skills": [
   "Corporate Travel Management",
   "Crisis Management",
   "GDS Systems (Sabre, Amadeus)",
   "Client Relationship Management",
   "Route/Cost Optimization",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines long client-service and travel-operations experience with new digital-marketing skills — suited to marketing or customer-marketing roles in travel/hospitality where client understanding is an asset.",
  "recommended_roles": [
   "Digital Marketing Executive (Travel / Hospitality)",
   "Customer / CRM Marketing Executive",
   "Marketing Coordinator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Deep service background but marketing is new; entry-to-mid marketing roles in travel/hospitality fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Jane Pang Siew Luan (Feng Xiuluan)",
  "email": "XIULUAN@GMAIL.COM",
  "years_experience": "15+",
  "industry_background": "Business operations & customer service (retail)",
  "prior_experience_summary": "15+ years in customer-service and business-operations at Popular and Crystal Jade, with SAP/Ariba/Coupa, AR management and data-driven sales reporting.",
  "skills": [
   "Business Operations",
   "Customer Service Leadership",
   "ERP (SAP, Ariba, Coupa)",
   "Sales Reporting & Analysis",
   "Stakeholder Liaison",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines operations, customer-service leadership and sales-reporting experience with new digital-marketing skills — suited to marketing-operations, CRM or campaign-support roles that reward process and data discipline.",
  "recommended_roles": [
   "Marketing Operations Executive",
   "CRM / Customer Marketing Executive",
   "Digital Marketing Coordinator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong ops/service background; marketing is new, so mid-level marketing-ops roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Jazreel Chua Sen Feng (Cai Senfeng)",
  "email": "jazreelchua@gmail.com",
  "years_experience": "15+",
  "industry_background": "Business operations, FMCG distribution & IT",
  "prior_experience_summary": "Managing Director of an FMCG distribution business plus earlier software-engineering experience, spanning operations, SDLC, B2B networks and client engagement.",
  "skills": [
   "Business Operations & Leadership",
   "FMCG / B2B Distribution",
   "Software Development (background)",
   "Systems Analysis",
   "Client Engagement",
   "Digital Marketing (foundational)",
   "Analytical Thinking"
  ],
  "skill_marriage": "Combines entrepreneurial business-operations and technical/software background with new digital-marketing skills — suited to marketing roles for FMCG/retail or tech-enabled marketing and marketing-operations positions.",
  "recommended_roles": [
   "Digital Marketing Executive (FMCG / Retail)",
   "Marketing Operations / MarTech Executive",
   "Business Development & Marketing Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Entrepreneurial leader with tech background; marketing is new, so pitch at senior-IC with an ops/tech angle."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Lee Liang Wei Justin (Li LiangWei)",
  "email": "Bodykitworks@gmail.com",
  "years_experience": "15+",
  "industry_background": "Project & sales management (defense, manufacturing, automotive)",
  "prior_experience_summary": "15+ years as Project & Sales Manager securing multimillion-dollar B2B/government contracts, with tender management, KPI reporting and data-driven insights.",
  "skills": [
   "Project & Tender Management",
   "B2B Sales & Client Acquisition",
   "Contract Negotiation",
   "Stakeholder Engagement (Govt/Corporate)",
   "KPI Reporting & Data Insights",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines B2B/government sales and tender-management experience with new digital-marketing skills — suited to B2B, account-based or government-sector marketing roles that value complex-sales understanding.",
  "recommended_roles": [
   "B2B / Government Marketing Executive",
   "Account-Based Marketing Executive",
   "Marketing & Business Development Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior in complex B2B sales; marketing is new, so pitch at senior-sales-with-marketing level."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Lim Hui Min, Rachel",
  "email": "rachel2321@gmail.com",
  "years_experience": "30+",
  "industry_background": "Creative / art direction & brand design (media)",
  "prior_experience_summary": "30+ years as Art Director at Mediacorp, leading brand development, visual storytelling, cross-media campaigns and CMS publishing, expert in Adobe Creative Cloud.",
  "skills": [
   "Art Direction & Brand Design",
   "Visual Storytelling",
   "Adobe Creative Cloud",
   "Content Creation (GIF, video, infographics)",
   "Social Media Content",
   "CMS Publishing",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines deep creative/art-direction and brand-content experience with new digital-marketing skills — a strong fit for content-marketing, creative-lead or brand-marketing roles where visual storytelling drives engagement.",
  "recommended_roles": [
   "Content / Creative Marketing Lead",
   "Brand & Social Media Marketing Executive",
   "Digital Content Art Director"
  ],
  "seniority": "Senior IC / Team-Lead potential",
  "seniority_note": "Very senior creative; digital-marketing formalises an already strong content foundation — one of the stronger DM profiles for creative/content roles."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Lim Juay Peo",
  "email": "maxiscab@gmail.com",
  "years_experience": "14+",
  "industry_background": "IT desktop support & limousine business ownership",
  "prior_experience_summary": "14 years in IT desktop/network support plus running a limousine company since 2008, self-taught in Google Ads, SEO, SEM, Facebook and email marketing for lead generation.",
  "skills": [
   "IT Desktop & Network Support",
   "Google Ads / SEM",
   "SEO",
   "Social Media Marketing",
   "Email Marketing",
   "Lead Generation",
   "Microsoft Office / Copilot"
  ],
  "skill_marriage": "Combines IT-support and hands-on self-run digital-marketing (SEO/SEM for his own business) with formal digital-marketing training — suited to SME digital-marketing or performance-marketing roles.",
  "recommended_roles": [
   "Digital Marketing Executive (SME / Performance)",
   "SEO / SEM Executive",
   "Social Media & Lead Gen Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Practical self-taught marketing for his own business; entry-to-mid marketing roles fit as he formalises the skills."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Lye Chin Chye",
  "email": "andrewandrew1980@hotmail.com",
  "years_experience": "10+",
  "industry_background": "Debt collection & business services",
  "prior_experience_summary": "Founder/Debt Collection Officer since 2013 handling sales support, client engagement and self-run digital marketing, plus valet-parking service work.",
  "skills": [
   "Client Engagement & Business Development",
   "Debt Collection & Negotiation",
   "Digital Marketing (foundational)",
   "Customer Handling",
   "Conflict Resolution",
   "Communication"
  ],
  "skill_marriage": "Combines client-engagement and negotiation experience with new digital-marketing skills — suited to entry-level marketing, business-development or SME outreach roles.",
  "recommended_roles": [
   "Digital Marketing Executive (SME)",
   "Business Development / Outreach Executive",
   "Marketing & Sales Support Executive"
  ],
  "seniority": "Entry",
  "seniority_note": "Brief CV, limited formal marketing; entry-level marketing/BD roles fit best."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Mohammad Burhan Bin Abdul Khalip",
  "email": "agentburhankhalip@gmail.com",
  "years_experience": "16+",
  "industry_background": "Real estate sales & aircraft maintenance",
  "prior_experience_summary": "16+ years as a top-tier real estate consultant at PropNex (Platinum Award, Top 20% producer), with prior aircraft-maintenance supervision at SIAEC.",
  "skills": [
   "Real Estate Sales & Investment Advisory",
   "Financial Modelling (property)",
   "Digital Targeting / Property Marketing",
   "Negotiation",
   "Market Analysis",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines award-winning property sales and digital-targeting experience with new formal digital-marketing skills — a strong fit for real-estate, property-tech or high-value-sales marketing roles.",
  "recommended_roles": [
   "Digital Marketing Executive (Real Estate / PropTech)",
   "Property Marketing & Lead Gen Executive",
   "Performance Marketing Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Strong sales producer with real digital-targeting experience; mid-to-senior marketing roles in property fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Norimah Binte Abdullah",
  "email": "norimahabd@gmail.com",
  "years_experience": "10+",
  "industry_background": "Media/advertising sales support & operations",
  "prior_experience_summary": "Senior Business Executive at SPH Media supporting marketing/media-solutions teams, monitoring cross-channel ad bookings, campaign schedules and Salesforce reporting.",
  "skills": [
   "Advertising Operations",
   "Campaign Coordination",
   "Salesforce / Ad Systems",
   "Sales Reporting & Analysis",
   "Social Media Marketing",
   "Gen AI Tools (ChatGPT, Gemini, Canva)",
   "Digital Marketing"
  ],
  "skill_marriage": "Combines media/advertising-operations and campaign-coordination experience with new digital-marketing and AI-tool skills — a natural fit for campaign-management, ad-operations or marketing-coordinator roles.",
  "recommended_roles": [
   "Campaign / Ad Operations Executive",
   "Digital Marketing Coordinator",
   "Marketing Operations Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Directly relevant advertising-ops background; mid-level marketing/campaign roles are a solid fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Richard Wong Chong Yee",
  "email": "Richardfaith18@hotmail.com",
  "years_experience": "20+",
  "industry_background": "Sales & technical/customer support (electronics, medical)",
  "prior_experience_summary": "Long sales career across electronics and Japanese-food distribution plus technical/customer-support roles, targeting a medical-equipment sales-support direction.",
  "skills": [
   "Sales & Business Development",
   "Customer Service",
   "Inventory & Logistics Coordination",
   "POS/Documentation",
   "Digital Marketing (foundational)",
   "Communication"
  ],
  "skill_marriage": "Combines long sales/customer-support experience with new digital-marketing skills — suited to sales-support marketing, product-marketing or SME marketing roles.",
  "recommended_roles": [
   "Digital Marketing / Sales Support Executive",
   "Product Marketing Executive",
   "Marketing Coordinator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Extensive but older sales experience; marketing is new, so entry-to-mid marketing roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0626",
  "full_name": "Tan Mui Suan, Michelle (Chen Meixuan, Michelle) / Mrs Michelle Lee",
  "email": "mich-tan@hotmail.com",
  "years_experience": "10+",
  "industry_background": "B2B & pharmaceutical/media sales",
  "prior_experience_summary": "10+ years in business development and sales across pharma (DKSH) and property/media (EdgeProp), with CRM use, sales-deck creation and marketing-strategy design.",
  "skills": [
   "Business Development",
   "B2B & Pharma Sales",
   "CRM & Lead Management",
   "Media Solutions Selling",
   "Sales/Marketing Strategy",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines B2B/pharma sales and media-solutions experience with new digital-marketing skills — suited to healthcare/B2B marketing, media-marketing or account-based marketing roles.",
  "recommended_roles": [
   "Digital Marketing Executive (Healthcare / B2B)",
   "Media / Account-Based Marketing Executive",
   "Business Development & Marketing Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Sales-strong with media exposure; marketing is a fresh pivot, so mid-level marketing roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Chang Zhong Ming, Terence",
  "email": "terence_844@hotmail.com",
  "years_experience": "10+",
  "industry_background": "Accounts payable & finance (multi-industry)",
  "prior_experience_summary": "10+ years in accounts-payable and finance across aerospace, tech and F&B, with full-cycle AP, reconciliations and ERP systems (SAP, Oracle Fusion, Xero).",
  "skills": [
   "Accounts Payable & GL",
   "Financial Reconciliation & Reporting",
   "ERP (SAP, Oracle Fusion, Xero)",
   "Advanced Excel (Pivot, XLOOKUP)",
   "Data Analysis (foundational)",
   "Audit Support"
  ],
  "skill_marriage": "Combines finance/AP and ERP-data experience with new data-science skills — suited to finance-analytics or reporting-analyst roles where accounting-data fluency strengthens the analysis.",
  "recommended_roles": [
   "Finance Data Analyst",
   "Reporting / Reconciliation Analyst",
   "Junior Data Analyst (Finance)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Solid finance/ERP data background; data science is new, so mid-level finance-analytics roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Chor Seng Huat (Cao Shengfa)",
  "email": "dirnko@hotmail.com",
  "years_experience": "20+",
  "industry_background": "Sales & operations (biomedical, multimedia)",
  "prior_experience_summary": "Senior Sales Executive at N&E Innovations managing a team of 8, sales operations, events and setup, with a multimedia-arts/3D-animation background.",
  "skills": [
   "Sales & Business Development",
   "Operations Setup",
   "Team Management",
   "Multimedia / 3D Design",
   "Data Analysis (foundational)",
   "Power BI (foundational)",
   "Reporting"
  ],
  "skill_marriage": "Combines sales-operations and creative-multimedia experience with new data-science skills — suited to sales-analytics or operations-analyst roles, or data-visualisation-leaning positions.",
  "recommended_roles": [
   "Sales / Business Data Analyst",
   "Data Visualisation Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Sales/ops background; data science is a significant pivot, so entry-to-mid analyst roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Jimmy Loke Chee Jin",
  "email": "jimdaloker@yahoo.com",
  "years_experience": "25+",
  "industry_background": "Technical sales & business development (oil & gas, subsea)",
  "prior_experience_summary": "25+ years in strategic sales, business development and technical operations across oil & gas, subsea and maritime sectors, with CRM/ERP proficiency and APAC market knowledge.",
  "skills": [
   "Strategic Sales & Business Development",
   "Technical / Subsea Systems",
   "CRM & ERP (Navision, Monday.com)",
   "Contract Negotiation",
   "Stakeholder Management",
   "Data Analysis (foundational)",
   "Sales Forecasting"
  ],
  "skill_marriage": "Combines senior technical-sales and business-development experience with new data-science skills — suited to sales-analytics, commercial-analyst or business-analyst roles in technical/industrial sectors.",
  "recommended_roles": [
   "Sales / Commercial Analyst",
   "Business Analyst (Technical Sales)",
   "Data Analyst (Industrial / Energy)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Very senior in technical sales; data science is new, so pitch analytics/BA roles at senior-IC with domain depth."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Kalis Ho Wei Yoke (He Huiyu)",
  "email": "kalishwy@hotmail.com",
  "years_experience": "8+",
  "industry_background": "Business operations & administration (govt/corporate)",
  "prior_experience_summary": "8+ years in operations coordination, KPI tracking and reporting at MOM and corporate roles, with Excel-based reporting, audits and team supervision.",
  "skills": [
   "Business Process Coordination",
   "KPI Monitoring & Reporting",
   "Excel / Data Entry",
   "Operational Reporting",
   "Data Analysis (foundational)",
   "Power BI (foundational)",
   "Stakeholder Engagement"
  ],
  "skill_marriage": "Combines operations-reporting and KPI-tracking experience with new data-science skills — suited to operations-analyst or reporting-analyst roles that turn operational data into insight.",
  "recommended_roles": [
   "Operations / Reporting Analyst",
   "Business Data Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Reporting/KPI exposure helps; data science is new, so entry-to-mid analyst roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Lai Foo Hwa, Tommy (Li Fuhua, Tommy)",
  "email": "t2lai_@live.com",
  "years_experience": "15+",
  "industry_background": "Call-centre / retail team leadership & QS",
  "prior_experience_summary": "Team-leadership and floor-management experience across Microsoft call centre and retail, plus quantity-surveying background, coaching teams and hitting sales targets.",
  "skills": [
   "Team Leadership",
   "Call Centre / Customer Service",
   "Sales & Retail Operations",
   "Training & Coaching",
   "Data Analysis (foundational)",
   "Excel",
   "Reporting"
  ],
  "skill_marriage": "Combines team-leadership and customer-operations experience with new data-science skills — suited to operations-analyst or service-analytics roles where people/process understanding supports the data.",
  "recommended_roles": [
   "Operations / Service Data Analyst",
   "Business Analyst (Operations)",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Leadership/ops background; data science is a big pivot, so entry-to-mid analyst roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Ng Lai Fun, Lina (Wu Lifen)",
  "email": "lina_ng1@yahoo.com.sg",
  "years_experience": "15+",
  "industry_background": "Financial reporting & planning/control (electronics MNC)",
  "prior_experience_summary": "Manager in Sony's SEA Planning & Control division for 15+ years, handling transfer-pricing, financial analysis, data consolidation and management reporting.",
  "skills": [
   "Financial Reporting & Analysis",
   "Data Consolidation & Insights",
   "Process Optimization",
   "Cross-functional Collaboration",
   "Data Analytics (foundational)",
   "Power BI (foundational)",
   "Excel"
  ],
  "skill_marriage": "Combines managerial financial-analysis and data-consolidation experience with new data-science skills — a strong fit for finance-analytics, business-analyst or reporting-analyst roles grounded in real financial data.",
  "recommended_roles": [
   "Finance / Business Data Analyst",
   "Reporting & Analytics Analyst",
   "BI Analyst (Finance)"
  ],
  "seniority": "Senior IC / Team-Lead potential",
  "seniority_note": "Managerial finance-analysis background; as a data pivot, pitch finance-analytics at senior-IC level."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Tan Yong Chiat (Chen YongJie)",
  "email": "tanyongchiat@gmail.com",
  "years_experience": "15+",
  "industry_background": "EHS / safety management (construction, data centres)",
  "prior_experience_summary": "EHS Manager at CREC leading safety teams on data-centre and power-plant projects, running a Behaviour-Based Safety data system with monthly analysis.",
  "skills": [
   "EHS / Safety Management",
   "Behaviour-Based Safety Data Analysis",
   "Risk Assessment",
   "Incident Investigation",
   "Data Analysis (foundational)",
   "Excel",
   "Reporting"
  ],
  "skill_marriage": "Combines safety-management and hands-on safety-data-analysis (BBSO system) experience with new data-science skills — a niche fit for safety analytics, risk-data or EHS-analytics roles.",
  "recommended_roles": [
   "Safety / Risk Data Analyst",
   "EHS Analytics Analyst",
   "Data Analyst (Construction / Operations)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior EHS manager already using safety data; as a data pivot, safety-analytics roles at senior-IC fit well."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0626",
  "full_name": "Yogishwarie D/O Viramohan",
  "email": "valenyogish@gmail.com",
  "years_experience": "3+",
  "industry_background": "Retail management",
  "prior_experience_summary": "Retail Manager at Woodlands Xpress handling store operations, inventory control, staff management, promotions and POS-based inventory analysis.",
  "skills": [
   "Retail Operations Management",
   "Inventory Control",
   "Merchandise Planning",
   "Staff Management",
   "Data Analysis (foundational)",
   "POS / Excel",
   "Reporting"
  ],
  "skill_marriage": "Combines retail-operations and inventory-analysis experience with new data-science skills — suited to retail-analytics or operations-analyst roles turning store/inventory data into insight.",
  "recommended_roles": [
   "Retail / Operations Data Analyst",
   "Inventory / Merchandising Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Retail-ops background; data science is new, so entry-to-mid analyst roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Bessie Lee Jing Yu (Li Jingyu)",
  "email": "lee_bessie@yahoo.com.sg",
  "years_experience": "21+",
  "industry_background": "Telecommunications & ICT enterprise/government sales",
  "prior_experience_summary": "21+ years in telecom/ICT enterprise and government B2B sales, tender management and strategic accounts (MINDEF, DSTA, MOH, A*STAR).",
  "skills": [
   "Enterprise & Government B2B Sales",
   "Tender & Proposal Management (GeBiz)",
   "ICT Solutions",
   "Account Management",
   "Stakeholder Engagement",
   "Digital Innovation Tools (foundational)",
   "Market Analysis"
  ],
  "skill_marriage": "Combines enterprise/government ICT-sales and tender experience with new digital-innovation skills — suited to digital-solutions sales, business-development or client-facing transformation roles in tech/govtech.",
  "recommended_roles": [
   "Digital Solutions / Business Development Executive",
   "Business Analyst (ICT / GovTech)",
   "Digital Transformation Consultant (Sales-facing)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Very senior in ICT sales; digital-innovation is new, so pitch solutions/BD or transformation roles at senior-IC."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Judy Tan Geok Mui (Chen Yumei, Judy)",
  "email": "tangmjudy@gmail.com",
  "years_experience": "15+",
  "industry_background": "Regional sales & business operations (FMCG/food)",
  "prior_experience_summary": "15+ years in regional sales management, customer service and business operations across Malaysia/Vietnam, leading sales teams and key accounts.",
  "skills": [
   "Regional Sales Management",
   "Business Operations",
   "Team Leadership",
   "Key Account Management",
   "Customer Service",
   "Digital Innovation Tools (foundational)",
   "Process Improvement"
  ],
  "skill_marriage": "Combines regional-sales and operations-leadership experience with new digital-innovation skills — suited to sales-operations-digitalisation, business-analyst or transformation-support roles.",
  "recommended_roles": [
   "Business / Operations Analyst",
   "Sales Operations Transformation Executive",
   "Digital Innovation Support Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior in regional sales/ops; digital-innovation is new, so pitch analytics/transformation at senior-IC."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Kong Chun Leong Edwin",
  "email": "edwinkcl@gmail.com",
  "years_experience": "20+",
  "industry_background": "General management & property/operations",
  "prior_experience_summary": "20+ years as GM/Director across property management, operations and business development, founding and running property/coliving businesses with P&L ownership.",
  "skills": [
   "General Management & P&L",
   "Operations & Process Optimisation",
   "Business Development",
   "Team Leadership",
   "Project & Change Management",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines senior general-management and operations-optimisation experience with new digital-innovation skills — suited to operations-transformation, digital-business or process-innovation leadership roles.",
  "recommended_roles": [
   "Digital Transformation / Operations Consultant",
   "Business / Process Innovation Manager",
   "Project Manager (Digital Transformation)"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior GM/founder; best positioned in transformation-lead or management roles leveraging operations depth."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Lee Yan Jin, Jenny",
  "email": "",
  "years_experience": "15+",
  "industry_background": "Sales & service operations (medical/scientific equipment)",
  "prior_experience_summary": "Sales & service operations specialist at Carl Zeiss and Thermo Fisher, implementing process automation, a QR-code digitalisation project and CRM improvements.",
  "skills": [
   "Sales & Service Operations",
   "Process Automation",
   "CRM (Next-Gen)",
   "Order Management (SAP, Oracle, Salesforce)",
   "Digitalisation Projects",
   "Digital Innovation Tools (foundational)",
   "Data Accuracy"
  ],
  "skill_marriage": "Combines service-operations and hands-on digitalisation-project experience (automation, QR-code process) with new digital-innovation skills — a good fit for process-automation, business-analyst or digital-operations roles.",
  "recommended_roles": [
   "Process Automation / Digital Operations Analyst",
   "Business Analyst (Service Operations)",
   "Digital Transformation Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Already ran digitalisation projects; mid-level automation/BA roles are a genuine fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Nassim Benamra",
  "email": "nassim.ben@mail.com",
  "years_experience": "10+",
  "industry_background": "Education, customer support & business development (tech, Middle East market)",
  "prior_experience_summary": "10+ years across education, VIP customer support at Tencent, business development at Elite Asia and language lecturing at NTU, focused on the Middle East market.",
  "skills": [
   "Customer Support (VIP/Online)",
   "Business Development",
   "Cross-Cultural Communication",
   "Team Leadership",
   "Training / Lecturing",
   "Digital Innovation Tools (foundational)",
   "Stakeholder Engagement"
  ],
  "skill_marriage": "Combines multilingual customer-support, business-development and teaching experience with new digital-innovation skills — suited to customer-experience-digitalisation, business-analyst or digital-support roles, especially for MENA markets.",
  "recommended_roles": [
   "Digital Customer Experience / Support Analyst",
   "Business Development & Digital Executive",
   "Business Analyst (Digital Services)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Varied support/BD background; digital-innovation is new, so mid-level roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Ng Chee Yen (Wu Ziying)",
  "email": "ncheeyen@hotmail.com",
  "years_experience": "17",
  "industry_background": "Project & commercial management (engineering/EPC)",
  "prior_experience_summary": "17 years delivering complex multi-vendor engineering programmes, most recently Project Financial Analyst at Rotary Engineering, owning budget tracking, forecasting and variance reporting.",
  "skills": [
   "Project & Programme Management",
   "Financial Control & Forecasting",
   "Variance Reporting",
   "Vendor Procurement",
   "Risk & Change Management",
   "Digital Innovation Tools (foundational)",
   "Data Analysis"
  ],
  "skill_marriage": "Combines project/commercial-management and financial-control experience with new digital-innovation skills — suited to project-analytics, PMO-digitalisation or business-analyst roles in engineering/EPC.",
  "recommended_roles": [
   "Project / Business Analyst (Engineering)",
   "PMO / Project Analytics Analyst",
   "Digital Transformation Analyst"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Strong project/financial-control background; digital-innovation new, so pitch analytics/BA at senior-IC."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Ng Song Wah",
  "email": "Songwah.apv@gmail.com",
  "years_experience": "25+",
  "industry_background": "IT leadership & venture philanthropy",
  "prior_experience_summary": "14 years IT leadership at IBM and Sun/Oracle (strategy, operations, regional business director) then Executive Director of a venture-philanthropy organisation since 2011.",
  "skills": [
   "IT Strategy & Operations",
   "Business Leadership",
   "Programme / Grant Management",
   "Stakeholder Engagement",
   "Impact Assessment",
   "Digital Innovation Tools (foundational)",
   "Change Management"
  ],
  "skill_marriage": "Combines senior IT-leadership and social-sector-programme experience with new digital-innovation skills — suited to digital-transformation, social-impact-tech or programme-innovation leadership roles.",
  "recommended_roles": [
   "Digital Transformation / Innovation Lead",
   "Programme / Business Analyst (Social Impact / Tech)",
   "Digital Strategy Consultant"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior IT and NGO leader; best in transformation/strategy roles rather than hands-on tooling."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Rachel Lee Cheau Eng",
  "email": "Rachel.lce77@gmail.com",
  "years_experience": "20+",
  "industry_background": "Finance & accounting (multi-industry MNC)",
  "prior_experience_summary": "20+ years in finance/accounting (AR, AP, GL, month-end close) across manufacturing, life sciences, IT and retail, with Oracle, SAP and OneStream.",
  "skills": [
   "Accounts Receivable / Payable & GL",
   "Month-End Closing",
   "ERP (Oracle, SAP, OneStream)",
   "Reconciliation & Reporting",
   "Credit Control",
   "Digital Innovation Tools (foundational)",
   "Process Automation (foundational)"
  ],
  "skill_marriage": "Combines deep finance/accounting and ERP experience with new digital-innovation skills — suited to finance-transformation, finance-process-automation or finance-systems business-analyst roles.",
  "recommended_roles": [
   "Finance Transformation / Process Automation Analyst",
   "Business Analyst (Finance Systems)",
   "Finance Digitalisation Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior finance professional; digital-innovation is new, so pitch finance-transformation/BA at senior-IC."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Sam Ho Jong Sem",
  "email": "hoo_family2000@yahoo.com.sg",
  "years_experience": "20+",
  "industry_background": "IT management & IT project management (logistics)",
  "prior_experience_summary": "IT Manager/Project Manager at DHL and Toll, managing IT accounts, cross-functional teams, contract negotiation and APAC solution delivery.",
  "skills": [
   "IT Project Management",
   "Client & Account Management",
   "Technical Solutions Consultation",
   "Team Leadership",
   "Contract Negotiation",
   "Digital Innovation Tools (foundational)",
   "Service Delivery"
  ],
  "skill_marriage": "Combines IT-project-management and client-solutions experience with new digital-innovation skills — a strong fit for digital-project-management, business-analyst or transformation-delivery roles.",
  "recommended_roles": [
   "Digital Project Manager",
   "Business Analyst (IT / Digital)",
   "Digital Transformation Delivery Lead"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior IT/PM background; genuinely ready for digital-PM or transformation-delivery roles."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Soh Bee Siong, Raymond (Su Meixiang)",
  "email": "raymondsbs1@gmail.com",
  "years_experience": "10+",
  "industry_background": "Transport operations management (public transport)",
  "prior_experience_summary": "Interchange Manager at SBS Transit handling bus-captain performance, data/trend analysis of feedback and operations management, with a Business degree and Internet-Computing diploma.",
  "skills": [
   "Transport Operations Management",
   "Data & Trend Analysis",
   "Performance Management",
   "Problem Solving",
   "Digital Innovation Tools (foundational)",
   "Process Improvement"
  ],
  "skill_marriage": "Combines transport-operations and data-analysis experience with new digital-innovation skills — suited to operations-analytics, process-improvement or transformation-support roles in transport/logistics.",
  "recommended_roles": [
   "Operations / Business Analyst (Transport)",
   "Process Improvement / Transformation Analyst",
   "Digital Innovation Support Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Operations-management background with some data work; mid-level analytics/transformation roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Syed Mohamed Bin Zumri Al-Khairid",
  "email": "syedmd0801@gmail.com",
  "years_experience": "35+",
  "industry_background": "Public sector, social enterprise & business development",
  "prior_experience_summary": "35+ years spanning public-sector leadership (People's Association), social-enterprise management and regional sales, with programme development and stakeholder engagement.",
  "skills": [
   "Stakeholder Engagement & Partnerships",
   "Programme Development",
   "Operations & Budget Management",
   "Business Development",
   "Community Leadership",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines long public-sector and social-enterprise leadership with new digital-innovation skills — suited to programme-digitalisation, community-tech or public-sector-transformation roles.",
  "recommended_roles": [
   "Programme / Digital Transformation Executive (Public Sector)",
   "Business Analyst (Community / Social Programmes)",
   "Digital Innovation Coordinator"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Very senior public-sector/social manager; digital-innovation is new, so pitch programme-transformation at senior level."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Tan Jie Yi (Karyne)",
  "email": "",
  "years_experience": "20+",
  "industry_background": "Corporate sales & early-childhood education/operations",
  "prior_experience_summary": "20+ years in corporate sales/customer engagement plus 10+ years in early-childhood education, leading centre operations, teams and programme delivery.",
  "skills": [
   "Centre / Operations Management",
   "Staff Leadership & Workforce Planning",
   "Programme Design",
   "Budget & Cost Control",
   "Customer Relationship Management",
   "Digital Innovation Tools (foundational)",
   "Change Management"
  ],
  "skill_marriage": "Combines commercial-sales and education-operations leadership with new digital-innovation skills — suited to operations-digitalisation, programme-transformation or business-analyst roles in education or services.",
  "recommended_roles": [
   "Operations / Programme Transformation Executive",
   "Business Analyst (Education / Services)",
   "Digital Innovation Coordinator"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior operations/programme leader; digital-innovation is new, so pitch transformation/BA at senior-IC."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0626",
  "full_name": "Wong Yu Qing, Serene",
  "email": "sereneyuqing@gmail.com",
  "years_experience": "20+",
  "industry_background": "Sales & marketing (paints/coatings, healthcare, retail)",
  "prior_experience_summary": "Sales & Marketing Assistant Manager at AkzoNobel with 20+ years in sales, business development and CRM across coatings, healthcare and luxury retail, using digitalisation for customer engagement.",
  "skills": [
   "Strategic Sales & Business Development",
   "Key Account Management",
   "Marketing & Customer Engagement",
   "Market Analysis",
   "Digital Innovation Tools (foundational)",
   "Data-Driven Decision Making",
   "Project Management"
  ],
  "skill_marriage": "Combines sales-and-marketing management with new digital-innovation skills — suited to sales/marketing-digitalisation, customer-engagement-transformation or business-analyst roles.",
  "recommended_roles": [
   "Sales / Marketing Transformation Executive",
   "Business Analyst (Commercial)",
   "Digital Innovation / Customer Engagement Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior sales/marketing manager; digital-innovation is new, so pitch transformation/BA at senior-IC."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDFSWD",
  "course_name": "Professional Diploma in Full Stack Web Development",
  "cohort": "WD-0626",
  "full_name": "Vincent See Kok Wing (Shi Guorong)",
  "email": "vincentsee2000@yahoo.com",
  "years_experience": "20+",
  "industry_background": "Network engineering & IT infrastructure",
  "prior_experience_summary": "Network engineer with a Network Computing degree and extensive certifications (CCNP, AWS, RedHat, Juniper), experienced in multi-vendor networking, firewalls, routing and switching.",
  "skills": [
   "Network Engineering (CCNP)",
   "Cloud (AWS)",
   "Linux (RHCSA)",
   "Security (Firewalls, VPN)",
   "IT Infrastructure",
   "Web Development (learning)",
   "Routing & Switching"
  ],
  "skill_marriage": "Combines deep network-engineering and infrastructure certifications with new full-stack web-development skills — well positioned for DevOps, backend/infrastructure-development or full-stack roles with strong networking grounding.",
  "recommended_roles": [
   "Full Stack / Backend Developer (Infra background)",
   "DevOps / Cloud Engineer",
   "Application / Systems Developer"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Strong network/infra credentials; web-dev is new, so junior-to-mid developer or DevOps roles leveraging infra depth fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDFSWD",
  "course_name": "Professional Diploma in Full Stack Web Development",
  "cohort": "WD-0626",
  "full_name": "Yeow Tze Khiam, Thomas (Yao Sijian)",
  "email": "thomasytk.econs@gmail.com",
  "years_experience": "5+",
  "industry_background": "Education / tutoring & learning-hub management",
  "prior_experience_summary": "Home tutor and learning-hub manager teaching JC/secondary Mathematics, managing accounts and building/maintaining an online-education webpage and content.",
  "skills": [
   "Teaching / Content Design",
   "Web Content Creation & Maintenance",
   "Mathematics / Problem Solving",
   "Administration",
   "Web Development (learning)",
   "Customer Communication"
  ],
  "skill_marriage": "Combines teaching, strong mathematics/logic and website-content experience with new full-stack web-development skills — suited to junior web-developer or edtech-development roles where logical thinking helps.",
  "recommended_roles": [
   "Junior Full Stack / Web Developer",
   "Front-End Developer (EdTech)",
   "Web Content / Application Developer"
  ],
  "seniority": "Entry",
  "seniority_note": "Career-changer from tutoring with some web-content work; entry-level developer roles fit best."
 },
 {
  "specialist": "Preetika",
  "course_code": "PDCA",
  "course_name": "Professional Diploma in Cloud Administration",
  "cohort": "CA-0626",
  "full_name": "Benjamin Poh Bingzhong",
  "email": "Benpoh86@gmail.com",
  "years_experience": "8+",
  "industry_background": "IT support & administration (infrastructure)",
  "prior_experience_summary": "IT Administrator since 2017 (career switch from engineering), managing M365/Entra/Azure, security policies, IT assets and endpoint configuration.",
  "skills": [
   "IT Administration",
   "Microsoft 365 / Entra / Azure",
   "IT Security (Defender)",
   "Endpoint & Asset Management",
   "Cloud Administration (learning)",
   "Troubleshooting",
   "Vendor Management"
  ],
  "skill_marriage": "Combines hands-on IT-administration and M365/Azure experience with new cloud-administration skills — well positioned for cloud-admin, cloud-support or systems-administrator roles building on real Azure exposure.",
  "recommended_roles": [
   "Cloud Administrator / Cloud Support Engineer",
   "Systems Administrator (Azure/M365)",
   "IT Infrastructure Engineer"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Genuine IT-admin and Azure/M365 experience; cloud-admin formalises it, so mid-level cloud-admin roles are a real fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "ACIS",
  "course_name": "Advanced Certificate in Infrastructure Support",
  "cohort": "EIT-0626",
  "full_name": "Fong Chee Meng (Fang Zhiming)",
  "email": "wesjkr2@gmail.com",
  "years_experience": "5+",
  "industry_background": "Retail sales & technical troubleshooting (Apple products)",
  "prior_experience_summary": "Mac Sales Representative at Elush with technical troubleshooting and customer service, plus independent cryptocurrency trading and market analysis.",
  "skills": [
   "Technical Troubleshooting",
   "Retail Sales & Customer Service",
   "Apple Product Support",
   "Market Analysis",
   "IT Infrastructure Support (learning)",
   "Communication"
  ],
  "skill_marriage": "Combines tech-product troubleshooting and customer-service experience with new infrastructure-support skills — suited to IT service-desk, technical-support or desktop-support roles.",
  "recommended_roles": [
   "IT Service Desk / Technical Support",
   "Desktop Support Executive",
   "IT Support Executive"
  ],
  "seniority": "Entry",
  "seniority_note": "Tech-retail troubleshooting helps but no formal IT role; entry-level support roles fit best."
 },
 {
  "specialist": "Preetika",
  "course_code": "ACIS",
  "course_name": "Advanced Certificate in Infrastructure Support",
  "cohort": "EIT-0626",
  "full_name": "Jenny Lee Peijuan (Li Peijuan)",
  "email": "lee.peijuanjenny@hotmail.com",
  "years_experience": "10+",
  "industry_background": "Admin & facilities management",
  "prior_experience_summary": "Admin & Facilities Executive at Takasago managing renovation projects, contractors, budgeting and authority submissions, with broad administrative operations experience.",
  "skills": [
   "Admin & Facilities Management",
   "Project Coordination",
   "Vendor Negotiation",
   "Budgeting",
   "IT Infrastructure Support (learning)",
   "Documentation"
  ],
  "skill_marriage": "Combines facilities/admin project-coordination experience with new infrastructure-support skills — suited to IT operations-coordination, IT-facilities or service-desk support roles.",
  "recommended_roles": [
   "IT Operations / Facilities Support Coordinator",
   "IT Service Desk / Support Executive",
   "Desktop Support Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Admin/facilities background; IT-domain is new, so entry-to-mid IT-support/coordination roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "ACIS",
  "course_name": "Advanced Certificate in Infrastructure Support",
  "cohort": "EIT-0626",
  "full_name": "Khoo Chian Huey Charmaine",
  "email": "chariskch@gmail.com",
  "years_experience": "20+",
  "industry_background": "Airline cabin crew / service operations",
  "prior_experience_summary": "20+ years as Singapore Airlines cabin crew, handling passenger data, onboard sales records, inventory tracking and compliance procedures, seeking an IT-infrastructure transition.",
  "skills": [
   "Service Operations",
   "Data Entry & Record-Keeping",
   "Inventory Tracking",
   "Compliance & Procedures",
   "IT Infrastructure Support (learning)",
   "Customer Service"
  ],
  "skill_marriage": "Combines long service-operations and procedural-compliance experience with new infrastructure-support skills — suited to IT service-desk or support roles where service discipline and customer handling are assets.",
  "recommended_roles": [
   "IT Service Desk / Helpdesk Support",
   "Desktop Support Executive",
   "IT Support Executive (Junior)"
  ],
  "seniority": "Entry",
  "seniority_note": "Career-changer with no prior IT role; entry-level support roles with training fit best."
 },
 {
  "specialist": "Preetika",
  "course_code": "ACIS",
  "course_name": "Advanced Certificate in Infrastructure Support",
  "cohort": "EIT-0626",
  "full_name": "Tan Soon Beng, Vernard (Chen Shunming)",
  "email": "verlion88@yahoo.com",
  "years_experience": "18+",
  "industry_background": "Retail, telecom & ICT sales",
  "prior_experience_summary": "18+ years in retail/corporate sales including telecom/ICT (Geenet), B2B/B2C consultative sales, plus recent PHV driving.",
  "skills": [
   "ICT / Telecom Sales",
   "B2B & B2C Sales",
   "Customer Service",
   "Consultative Solutions",
   "IT Infrastructure Support (learning)",
   "Communication"
  ],
  "skill_marriage": "Combines ICT/telecom sales and customer-service experience with new infrastructure-support skills — suited to IT service-desk, IT-sales-support or technical-support roles where customer handling is valued.",
  "recommended_roles": [
   "IT Service Desk / Support Executive",
   "IT Sales / Pre-Sales Support",
   "Desktop Support Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "ICT-sales exposure helps context; hands-on IT is new, so entry-to-mid support roles fit."
 },
 {
  "specialist": "Preetika",
  "course_code": "ACIS",
  "course_name": "Advanced Certificate in Infrastructure Support",
  "cohort": "EIT-0626",
  "full_name": "Tang Han Yao",
  "email": "fujima756@hotmail.com",
  "years_experience": "15+",
  "industry_background": "Electrical / facilities engineering (data centres)",
  "prior_experience_summary": "Shift Facilities Engineer at Princeton Digital Group maintaining data-centre M&E systems, with PLC, BMS and electrical-engineering background across multiple diplomas.",
  "skills": [
   "Electrical / Facilities Engineering",
   "Data Centre M&E Systems",
   "PLC & BMS",
   "Technical Troubleshooting",
   "IT Infrastructure Support (learning)",
   "Wiring Schematics"
  ],
  "skill_marriage": "Combines data-centre facilities-engineering and technical-systems experience with new infrastructure-support skills — a strong fit for data-centre-operations, infrastructure-support or facilities-IT roles.",
  "recommended_roles": [
   "Data Centre / Infrastructure Support Engineer",
   "Facilities / M&E Technician (IT)",
   "IT Infrastructure Support Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Directly relevant data-centre/facilities engineering; infra-support is a natural adjacency, so mid-level DC/infra roles fit well."
 }
]
