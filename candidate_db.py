"""
Pre-loaded candidate database for TalentConnect.

Real candidates classified once using the Skill Marriage method
(prior experience x new course skills -> unique value, recommended roles,
seniority) plus a primary domain family. PDPA: only full name and email are
kept as identifiers; DOB, address, NRIC, gender, photo and phone are excluded.

This data is bundled with the app so it is always present and survives reboots.
Grown monthly by appending new classified cohorts to CANDIDATE_DB.
"""

# Course code -> short label
COURSES = {
    "PDDM": "Digital Marketing",
    "PDDS": "Data Science",
    "PDDI": "Digital Innovation",
    "PDFSWD": "Full Stack Web Development",
    "PDCA": "Cloud Administration",
    "ACIS": "Infrastructure Support",
}

# Domain families (primary domain knowledge, independent of course)
DOMAINS = [
 "Banking & Wealth",
 "EHS & Safety",
 "Education & Training",
 "Engineering & Manufacturing",
 "Finance & Accounting",
 "General Management",
 "HR & Talent",
 "IT & Infrastructure",
 "Marketing & Creative",
 "Operations & Admin",
 "Project Management",
 "Public Sector & Social",
 "Real Estate",
 "Sales & Business Development",
 "Supply Chain & Procurement"
]

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
  "seniority_note": "Genuinely senior with MBA, presales leadership and MarTech depth — one of the stronger profiles for a strategy/consulting-level marketing role.",
  "domain": "IT & Infrastructure"
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
  "seniority_note": "Long tenure is administrative rather than marketing-lead; position as a dependable marketing-ops IC entering the field.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Self-employed marketing experience is practical but informal; entry-to-mid marketing roles fit well.",
  "domain": "Real Estate"
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
  "seniority_note": "Sales-strong; marketing is new, so entry-to-mid marketing roles fit best.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Very senior in finance; as a marketing pivot, best positioned in data/ops-leaning marketing roles rather than creative/brand.",
  "domain": "Finance & Accounting"
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
  "seniority_note": "Extensive but admin/sales-based; marketing is new, so entry-level marketing roles in finance suit.",
  "domain": "Finance & Accounting"
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
  "seniority_note": "Strong ownership mindset but formal marketing depth is new; entry-to-mid marketing roles fit best.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Marketing degree plus sales gives a fair marketing foundation; mid-level marketing roles are realistic.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Senior in sales; digital-marketing execution is new, so pitch at senior-sales-with-marketing rather than marketing-lead.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Domain-strong but marketing is a fresh pivot; entry-level marketing roles in regulated sectors suit best.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Solid sales track record; marketing execution is new, so mid-level B2B marketing roles fit.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Brief CV; marketing experience is informal/self-driven, so entry-level marketing roles suit best.",
  "domain": "Real Estate"
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
  "seniority_note": "Domain is safety/security, not analytical; data science is a significant pivot, so entry-level analyst roles suit.",
  "domain": "EHS & Safety"
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
  "seniority_note": "Solid engineering experience; data science is new, so entry-to-mid analyst roles with domain context fit best.",
  "domain": "Engineering & Manufacturing"
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
  "seniority_note": "Strong data-handling exposure but analytics is new; entry-to-mid analyst roles with enterprise-systems context fit.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Senior HR practitioner; as a data pivot, people-analytics is the natural bridge role at senior-IC level.",
  "domain": "HR & Talent"
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
  "seniority_note": "Strong existing technical depth (SQL, ETL, BI); genuinely job-ready for mid-senior data roles.",
  "domain": "IT & Infrastructure"
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
  "seniority_note": "HR-metrics exposure gives a head start; data science is new, so mid-level people-analytics roles fit.",
  "domain": "HR & Talent"
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
  "seniority_note": "Senior in operations management; as a data pivot, pitch analytics roles at senior-IC with an operations-leadership angle.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Strong senior evidence; as a data-science pivot, pitch analytics roles at senior-IC rather than data-lead titles.",
  "domain": "Finance & Accounting"
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
  "seniority_note": "Genuinely senior PM; best positioned leading data/analytics delivery rather than hands-on data-scientist roles.",
  "domain": "Project Management"
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
  "seniority_note": "Technical-operations background with self-taught coding; genuine analytics experience is limited, so entry-level roles fit.",
  "domain": "Engineering & Manufacturing"
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
  "seniority_note": "Operations-strong but digital skills are new; entry-to-mid transformation-support roles fit best.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Strong wealth-sales record; digital-innovation is new, so mid-level fintech/BA roles fit.",
  "domain": "Banking & Wealth"
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
  "seniority_note": "Varied admin and analytical background; digital-innovation is new, so mid-level roles fit.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Led regional TA teams; strong domain, digital-innovation skills fresh — pitch HR-tech/analytics at senior-IC.",
  "domain": "HR & Talent"
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
  "seniority_note": "Prior data-viz training gives an edge; mid-level analytics/transformation roles in supply chain fit.",
  "domain": "Supply Chain & Procurement"
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
  "seniority_note": "Very senior operations leader; best positioned in transformation-lead roles leveraging manufacturing depth.",
  "domain": "Engineering & Manufacturing"
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
  "seniority_note": "Strong HR-systems exposure; digital-innovation skills are new, so mid-level HR-tech/BA roles fit.",
  "domain": "HR & Talent"
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
  "seniority_note": "Senior in procurement/engineering; digital-innovation is new, so pitch transformation/BA roles at senior-IC with domain depth.",
  "domain": "Supply Chain & Procurement"
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
  "seniority_note": "Solid infrastructure IC; digital-innovation/low-code is new, so entry-to-mid transformation-support roles fit.",
  "domain": "IT & Infrastructure"
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
  "seniority_note": "Genuinely senior banking leader; best positioned in transformation/consulting roles rather than hands-on tool building.",
  "domain": "Banking & Wealth"
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
  "seniority_note": "Strong Agile/product and data-translation background; genuinely ready for senior BA/product roles.",
  "domain": "Project Management"
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
  "seniority_note": "Real infra depth plus new dev skills; junior-to-mid developer or DevOps roles are a genuine fit.",
  "domain": "IT & Infrastructure"
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
  "seniority_note": "Strong hardware engineer; software dev is new, so junior-developer or hardware-software bridge roles fit.",
  "domain": "Engineering & Manufacturing"
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
  "seniority_note": "Commerce-strong; dev is new, so junior web-developer roles with an eCommerce angle fit best.",
  "domain": "Marketing & Creative"
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
  "seniority_note": "Very senior in operations; web-dev is a fresh add-on, so leverage it in a technical-leadership/transformation role, not junior developer.",
  "domain": "Engineering & Manufacturing"
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
  "seniority_note": "Senior engineer with strong discipline; IT infra is new, so pitch mid-level infra/support with an engineering-leadership angle.",
  "domain": "Engineering & Manufacturing"
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
  "seniority_note": "No prior IT role; infra skills are new, so entry-level support roles with training fit best.",
  "domain": "Operations & Admin"
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
  "seniority_note": "No prior IT role; infra skills are new, so entry-level service-desk/support roles fit best.",
  "domain": "IT & Infrastructure"
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
  "seniority_note": "Extremely experienced engineer but IT-domain is new; pitch mid-level infra-support leveraging troubleshooting depth.",
  "domain": "Engineering & Manufacturing"
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
  "seniority_note": "Significant career change with no IT background; entry-level support roles with training suit best.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Technical troubleshooting background helps, but IT-domain is new; entry-to-mid support roles fit.",
  "domain": "EHS & Safety"
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
  "seniority_note": "Senior in commercial/logistics; marketing is new. Note: CV states a Digital Innovation diploma though filed under DM — confirm course.",
  "domain": "Supply Chain & Procurement"
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
  "seniority_note": "Strong B2B sales; marketing is a fresh pivot, so mid-level B2B marketing roles fit.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Deep service background but marketing is new; entry-to-mid marketing roles in travel/hospitality fit.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Strong ops/service background; marketing is new, so mid-level marketing-ops roles fit.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Entrepreneurial leader with tech background; marketing is new, so pitch at senior-IC with an ops/tech angle.",
  "domain": "General Management"
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
  "seniority_note": "Senior in complex B2B sales; marketing is new, so pitch at senior-sales-with-marketing level.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Very senior creative; digital-marketing formalises an already strong content foundation — one of the stronger DM profiles for creative/content roles.",
  "domain": "Marketing & Creative"
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
  "seniority_note": "Practical self-taught marketing for his own business; entry-to-mid marketing roles fit as he formalises the skills.",
  "domain": "IT & Infrastructure"
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
  "seniority_note": "Brief CV, limited formal marketing; entry-level marketing/BD roles fit best.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Strong sales producer with real digital-targeting experience; mid-to-senior marketing roles in property fit.",
  "domain": "Real Estate"
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
  "seniority_note": "Directly relevant advertising-ops background; mid-level marketing/campaign roles are a solid fit.",
  "domain": "Marketing & Creative"
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
  "seniority_note": "Extensive but older sales experience; marketing is new, so entry-to-mid marketing roles fit.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Sales-strong with media exposure; marketing is a fresh pivot, so mid-level marketing roles fit.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Solid finance/ERP data background; data science is new, so mid-level finance-analytics roles fit.",
  "domain": "Finance & Accounting"
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
  "seniority_note": "Sales/ops background; data science is a significant pivot, so entry-to-mid analyst roles fit.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Very senior in technical sales; data science is new, so pitch analytics/BA roles at senior-IC with domain depth.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Reporting/KPI exposure helps; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Leadership/ops background; data science is a big pivot, so entry-to-mid analyst roles fit.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Managerial finance-analysis background; as a data pivot, pitch finance-analytics at senior-IC level.",
  "domain": "Finance & Accounting"
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
  "seniority_note": "Senior EHS manager already using safety data; as a data pivot, safety-analytics roles at senior-IC fit well.",
  "domain": "EHS & Safety"
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
  "seniority_note": "Retail-ops background; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Very senior in ICT sales; digital-innovation is new, so pitch solutions/BD or transformation roles at senior-IC.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Senior in regional sales/ops; digital-innovation is new, so pitch analytics/transformation at senior-IC.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Senior GM/founder; best positioned in transformation-lead or management roles leveraging operations depth.",
  "domain": "General Management"
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
  "seniority_note": "Already ran digitalisation projects; mid-level automation/BA roles are a genuine fit.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Varied support/BD background; digital-innovation is new, so mid-level roles fit.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Strong project/financial-control background; digital-innovation new, so pitch analytics/BA at senior-IC.",
  "domain": "Finance & Accounting"
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
  "seniority_note": "Senior IT and NGO leader; best in transformation/strategy roles rather than hands-on tooling.",
  "domain": "IT & Infrastructure"
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
  "seniority_note": "Senior finance professional; digital-innovation is new, so pitch finance-transformation/BA at senior-IC.",
  "domain": "Finance & Accounting"
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
  "seniority_note": "Senior IT/PM background; genuinely ready for digital-PM or transformation-delivery roles.",
  "domain": "IT & Infrastructure"
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
  "seniority_note": "Operations-management background with some data work; mid-level analytics/transformation roles fit.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Very senior public-sector/social manager; digital-innovation is new, so pitch programme-transformation at senior level.",
  "domain": "Public Sector & Social"
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
  "seniority_note": "Senior operations/programme leader; digital-innovation is new, so pitch transformation/BA at senior-IC.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Senior sales/marketing manager; digital-innovation is new, so pitch transformation/BA at senior-IC.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Strong network/infra credentials; web-dev is new, so junior-to-mid developer or DevOps roles leveraging infra depth fit.",
  "domain": "IT & Infrastructure"
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
  "seniority_note": "Career-changer from tutoring with some web-content work; entry-level developer roles fit best.",
  "domain": "Education & Training"
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
  "seniority_note": "Genuine IT-admin and Azure/M365 experience; cloud-admin formalises it, so mid-level cloud-admin roles are a real fit.",
  "domain": "IT & Infrastructure"
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
  "seniority_note": "Tech-retail troubleshooting helps but no formal IT role; entry-level support roles fit best.",
  "domain": "IT & Infrastructure"
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
  "seniority_note": "Admin/facilities background; IT-domain is new, so entry-to-mid IT-support/coordination roles fit.",
  "domain": "Operations & Admin"
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
  "seniority_note": "Career-changer with no prior IT role; entry-level support roles with training fit best.",
  "domain": "Operations & Admin"
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
  "seniority_note": "ICT-sales exposure helps context; hands-on IT is new, so entry-to-mid support roles fit.",
  "domain": "Sales & Business Development"
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
  "seniority_note": "Directly relevant data-centre/facilities engineering; infra-support is a natural adjacency, so mid-level DC/infra roles fit well.",
  "domain": "Engineering & Manufacturing"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0526",
  "full_name": "Khor Swee Aik",
  "email": "flame_aik@me.com",
  "years_experience": "25+",
  "industry_background": "Visual effects & post-production (media/film)",
  "prior_experience_summary": "VFX Director and founder of a visual-effects studio for 8+ years, plus senior VFX supervision at VHQ Media, directing creative pipelines, teams and client delivery.",
  "skills": [
   "Visual Effects & Motion Graphics",
   "Creative Direction",
   "Video Production",
   "Project Management",
   "Team Leadership",
   "Digital Marketing (foundational)",
   "Content Creation"
  ],
  "skill_marriage": "Combines deep visual-effects/creative-production leadership with new digital-marketing skills — can conceive and produce high-end video/visual content and run the campaigns around it, ideal for content-led or creative marketing roles.",
  "recommended_roles": [
   "Content / Video Marketing Lead",
   "Creative Marketing Executive",
   "Social Media & Multimedia Marketing Executive"
  ],
  "seniority": "Senior IC / Team-Lead potential",
  "seniority_note": "Very senior creative/production leader; digital-marketing formalises a strong content base — pitch content/creative marketing, not entry-level.",
  "domain": "Marketing & Creative"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0526",
  "full_name": "Samantha Lee Yu Zhen",
  "email": "samanthalyz@hotmail.com",
  "years_experience": "12+",
  "industry_background": "Human resources operations & shared services",
  "prior_experience_summary": "Senior HR Associate at Surbana Jurong and HR Associate Analyst at Accenture, handling HR operations, HRIS (SAP S/4HANA, Workday), employee data and training.",
  "skills": [
   "HR Operations",
   "HRIS (SAP S/4HANA, Workday)",
   "Employee Data Management",
   "Process Improvement",
   "Training & Communication",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines HR-operations and communications-degree background with new digital-marketing skills — suited to employer-branding, internal-communications or recruitment-marketing roles that bridge people and campaigns.",
  "recommended_roles": [
   "Employer Branding / Recruitment Marketing Executive",
   "Internal Communications & Marketing Executive",
   "Marketing Operations Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Solid HR-ops background; marketing is a fresh pivot, so mid-level marketing roles with an HR/comms angle fit.",
  "domain": "HR & Talent"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0526",
  "full_name": "Melvin Heng Kok Ann (Wang Guoan)",
  "email": "melvinheng@hotmail.com",
  "years_experience": "25+",
  "industry_background": "FMCG & alcohol commercial sales (SEA regional)",
  "prior_experience_summary": "25+ years in regional commercial sales and marketing across FMCG and alcohol, leading route-to-market strategy, distributor ecosystems and trade marketing across SEA, with strong e-commerce growth results.",
  "skills": [
   "Route-to-Market Strategy",
   "Distributor & Key Account Management",
   "Trade Marketing & Brand Activation",
   "Commercial Strategy",
   "E-commerce Growth",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines senior FMCG/alcohol commercial-sales and trade-marketing leadership with new digital-marketing skills — strong fit for brand, trade or commercial marketing roles that blend distribution knowledge with digital campaigns.",
  "recommended_roles": [
   "Trade / Brand Marketing Manager (FMCG)",
   "Commercial Marketing Executive",
   "E-commerce / Digital Marketing Executive"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Genuinely senior commercial leader; position at brand/trade marketing manager level, not entry marketing.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0526",
  "full_name": "Mandy Koh Hui Ping (Xu Huiping)",
  "email": "mandy.kohhp@gmail.com",
  "years_experience": "15+",
  "industry_background": "Executive/administrative support (banking)",
  "prior_experience_summary": "Team Assistant to MDs in wealth/retail banking at Standard Chartered, plus business-development-assistant experience, handling stakeholder coordination, events and procurement.",
  "skills": [
   "Executive & Administrative Support",
   "Stakeholder Coordination",
   "Event Organisation",
   "Procurement / Expense Processing",
   "Client Communication",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines strong administrative/stakeholder-coordination experience in banking with new digital-marketing skills — suited to marketing-operations, event-marketing or marketing-coordinator roles.",
  "recommended_roles": [
   "Marketing Operations / Coordinator",
   "Event Marketing Executive",
   "Marketing Administrator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Admin/coordination background; marketing is new, so entry-to-mid marketing-support roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0526",
  "full_name": "Cheah Soon Lee, Leslie (Xie Shunli)",
  "email": "leslie.cheah@sg-alliance.com",
  "years_experience": "13+",
  "industry_background": "Wealth management & insurance advisory",
  "prior_experience_summary": "13+ years in wealth management and insurance advisory (SG Alliance, AIA, Prudential), delivering financial planning, client acquisition and team mentoring, MDRT achiever.",
  "skills": [
   "Wealth & Financial Planning",
   "Client Relationship Management",
   "Insurance Advisory",
   "Business Development",
   "Team Leadership",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines financial-advisory and client-relationship experience with new digital-marketing skills — suited to marketing roles in financial services, or lead-generation/client-acquisition marketing.",
  "recommended_roles": [
   "Digital Marketing Executive (Financial Services)",
   "Lead Generation / Client Acquisition Marketing",
   "CRM Marketing Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong advisory/sales record; marketing is new, so mid-level marketing roles in finance fit.",
  "domain": "Banking & Wealth"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0526",
  "full_name": "Chong Mui Har, Michelle (Zhang Meixia)",
  "email": "chongmuihar01@gmail.com",
  "years_experience": "25+",
  "industry_background": "HR & administrative operations (public sector/defence)",
  "prior_experience_summary": "25+ years at MINDEF across HR execution, performance management for 1,500 personnel, events coordination and executive administration, with recent RPA and GenAI training.",
  "skills": [
   "HR Operations",
   "Performance Management",
   "Event Coordination",
   "Administrative Operations",
   "RPA (Basic) & GenAI tools",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines long HR/administrative public-sector experience with new digital-marketing and automation skills — suited to marketing-operations, internal-communications or HR/employer-branding-adjacent marketing roles.",
  "recommended_roles": [
   "Marketing Operations Executive",
   "Internal Communications / Employer Branding Executive",
   "Marketing Coordinator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Extensive HR/admin background; marketing is new, so entry-to-mid marketing-ops roles fit.",
  "domain": "HR & Talent"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0526",
  "full_name": "Juliyawati Binte Alatdin",
  "email": "juls08@gmail.com",
  "years_experience": "21+",
  "industry_background": "Quality assurance & operations coordination (maritime)",
  "prior_experience_summary": "21+ years as Group QA Coordinator in maritime/ship management, handling operations coordination, data reporting (Power BI, TM Master) and compliance documentation.",
  "skills": [
   "Operations Coordination",
   "Data Reporting & Analysis (Power BI)",
   "Documentation & Compliance",
   "Stakeholder Communication",
   "GenAI tools",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines maritime operations-coordination and data-reporting experience with new digital-marketing skills — suited to marketing-operations or data-leaning marketing-support roles where process and analytics discipline help.",
  "recommended_roles": [
   "Marketing Operations Executive",
   "Marketing Data / Reporting Executive",
   "Digital Marketing Coordinator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Long ops/QA background; marketing is a fresh pivot, so entry-to-mid marketing roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0526",
  "full_name": "Kelvin Cheong Kah Wing (Zhang Jiarong)",
  "email": "cheong.kelvin@gmail.com",
  "years_experience": "26",
  "industry_background": "Technical sales & service support (industrial/APAC)",
  "prior_experience_summary": "26 years in technical sales, service support and training across industrial equipment firms, managing APAC parts sales, distributor development and technical training.",
  "skills": [
   "Technical B2B Sales",
   "Distributor Development & Training",
   "Service & Warranty Support",
   "Product Launches",
   "Key Account Management",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines long technical B2B sales and distributor-training experience with new digital-marketing skills — suited to industrial/technical marketing, channel marketing or product-marketing roles.",
  "recommended_roles": [
   "Technical / Industrial Marketing Executive",
   "Channel / Distributor Marketing Executive",
   "Product Marketing Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior technical-sales professional; marketing is new, so pitch B2B/technical marketing at senior-IC.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0526",
  "full_name": "Koh Yeong Qi, Caren",
  "email": "care_caren@yahoo.com",
  "years_experience": "15+",
  "industry_background": "Executive support & customer service",
  "prior_experience_summary": "Executive Assistant to CEO/HODs and customer-service background, with a Marketing Management degree, handling secretarial support, travel, meetings and expense management.",
  "skills": [
   "Executive & Administrative Support",
   "Customer Service",
   "Event & Meeting Coordination",
   "Marketing Management (degree)",
   "Microsoft Office",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines executive-support and customer-service experience plus a marketing degree with refreshed digital-marketing skills — suited to marketing-coordinator, marketing-operations or event-marketing roles.",
  "recommended_roles": [
   "Marketing Coordinator / Operations Executive",
   "Event Marketing Executive",
   "Digital Marketing Assistant"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Admin/service background with a marketing degree; entry-to-mid marketing roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0526",
  "full_name": "Jesphine Low Pei Fang",
  "email": "jes.lpf@gmail.com",
  "years_experience": "20+",
  "industry_background": "Graphic design & print production (publishing)",
  "prior_experience_summary": "20+ years as Senior Graphic Designer at a publishing house, owning concept-to-layout design of books, maps and print collateral, expert in Adobe Creative Suite.",
  "skills": [
   "Graphic Design",
   "Adobe Creative Suite (Photoshop, InDesign, Illustrator)",
   "Layout & Print Production",
   "Illustration",
   "Content Creation",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines deep graphic-design and print-production experience with new digital-marketing skills — can both design creatives and run the campaigns, ideal for content/creative or social-media marketing roles without a designer handover.",
  "recommended_roles": [
   "Content / Creative Marketing Executive",
   "Social Media & Design Marketing Executive",
   "Digital Marketing Designer"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong design foundation; marketing is new, so mid-level content/creative marketing roles fit well.",
  "domain": "Marketing & Creative"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0526",
  "full_name": "Siti Aminah Binte Abu Bakar",
  "email": "sitiaminahabubakar@gmail.com",
  "years_experience": "10+",
  "industry_background": "Business development & partnerships (EdTech/SaaS)",
  "prior_experience_summary": "10+ years in business development and channel/corporate partnerships across EdTech and SaaS (VitalSource), driving APAC market expansion, go-to-market strategy and new client acquisition.",
  "skills": [
   "Business Development",
   "Partnership & Channel Management",
   "Go-to-Market Strategy",
   "SaaS / EdTech Solutions",
   "Key Account Management",
   "CRM (Salesforce)",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines B2B/SaaS business-development and go-to-market experience with new digital-marketing skills — strong fit for growth marketing, partnership marketing or demand-generation roles in tech/SaaS.",
  "recommended_roles": [
   "Growth / Demand Generation Marketing Executive",
   "Partnership Marketing Executive",
   "B2B / SaaS Marketing Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior BD/partnerships background; marketing is new, so pitch growth/B2B marketing at senior-IC.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0526",
  "full_name": "Tan Yoke Hong, Evon (Chen Yufeng)",
  "email": "yokehongtan@gmail.com",
  "years_experience": "16+",
  "industry_background": "Investment / equity research & real estate advisory",
  "prior_experience_summary": "CFA Charterholder and Chartered Accountant with 16+ years across equity research, fund management and data-driven real estate advisory, applying investment-grade analysis.",
  "skills": [
   "Equity Research & Valuation",
   "Financial Modelling",
   "Data-Driven Advisory",
   "Portfolio & Risk Analysis",
   "Real Estate Analysis",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines deep finance/investment-analysis and property-advisory expertise with new digital-marketing skills — suited to finance/property marketing, content-marketing for financial services, or analytical marketing roles.",
  "recommended_roles": [
   "Marketing Executive (Financial Services / PropTech)",
   "Content Marketing (Finance/Investment)",
   "Marketing Analytics Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Strong finance/analytical professional; marketing is new — best in analytical or finance-sector marketing rather than creative.",
  "domain": "Banking & Wealth"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Kwan Dickson",
  "email": "dickson.kwan@gmail.com",
  "years_experience": "13+",
  "industry_background": "Sales & operations (freight/logistics)",
  "prior_experience_summary": "13+ years in freight/logistics sales and operations at Embassy Freight, handling business development, freight-rate data analysis, pricing, quotations and sales reporting.",
  "skills": [
   "Sales & Business Development",
   "Freight Data Analysis",
   "Pricing & Cost Analysis",
   "Sales Reporting",
   "Excel",
   "Data Analysis (foundational)",
   "Power BI (foundational)"
  ],
  "skill_marriage": "Combines freight/logistics sales and pricing-data experience with new data-science skills — suited to logistics-analytics, pricing-analyst or sales-data-analyst roles grounded in real commercial data.",
  "recommended_roles": [
   "Data / Pricing Analyst (Logistics)",
   "Sales / Commercial Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Sales/ops with data exposure; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Damien Chong Wai Mun (Zhong WeiWen)",
  "email": "damienchongwm@gmail.com",
  "years_experience": "12+",
  "industry_background": "Analytics, dashboards & equity research (public sector/finance)",
  "prior_experience_summary": "Senior Executive at ITE building learner-progress dashboards and GenAI support tools, plus prior senior-analyst roles at ACRA and equity research at UOB Asset Management.",
  "skills": [
   "Dashboard Development",
   "Data Analysis & Reporting",
   "GenAI Tools",
   "Financial Modelling",
   "Process Improvement",
   "Power BI",
   "Stakeholder Management"
  ],
  "skill_marriage": "Combines dashboarding, analytics and equity-research experience with new data-science skills — one of the stronger DS profiles, genuinely ready for data-analyst or BI roles with real analytical track record.",
  "recommended_roles": [
   "Data Analyst / BI Analyst",
   "Business / Insights Analyst",
   "Junior Data Scientist"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Real analytics and dashboard experience plus finance background; job-ready for mid-level data roles.",
  "domain": "Finance & Accounting"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Muhammad Zameer Bin Ali",
  "email": "zameeriusmax52@gmail.com",
  "years_experience": "10+",
  "industry_background": "Data operations, retail & HR operations",
  "prior_experience_summary": "Team Lead (Data Ops) at PersolKelly managing data accuracy for national research, plus omnichannel/retail leadership and HR/POS operations experience.",
  "skills": [
   "Data Operations & Quality",
   "Team Leadership",
   "KPI & Performance Management",
   "E-commerce / Retail Ops",
   "SAP",
   "Data Analysis (foundational)",
   "Reporting"
  ],
  "skill_marriage": "Combines data-operations team leadership and retail/HR-ops experience with new data-science skills — suited to data-ops, data-quality-analyst or operations-analytics roles.",
  "recommended_roles": [
   "Data Operations / Quality Analyst",
   "Operations / Business Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Data-ops leadership helps; data science is new, so mid-level data-ops/analyst roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Tan Hao Jie, Nigel",
  "email": "haojie_tan@yahoo.com.sg",
  "years_experience": "9+",
  "industry_background": "Regional B2B sales (industrial electronics)",
  "prior_experience_summary": "9+ years as Regional Sales Executive at Panasonic Industry, driving market expansion, channel/partner management and competitor/market intelligence across APAC.",
  "skills": [
   "Regional B2B Sales",
   "Channel & Partner Management",
   "Market Intelligence",
   "Revenue Growth",
   "Data Analysis (foundational)",
   "Excel",
   "Reporting"
  ],
  "skill_marriage": "Combines regional B2B sales and market-intelligence experience with new data-science skills — suited to sales-analytics, commercial-analyst or market-data-analyst roles.",
  "recommended_roles": [
   "Sales / Commercial Analyst",
   "Market / Business Data Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Sales/market-intel background; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Tay Kar Yong, Kenny (Zheng JiaRong)",
  "email": "kennytay168@gmail.com",
  "years_experience": "15+",
  "industry_background": "Real estate sales & site engineering",
  "prior_experience_summary": "15+ years in Singapore real estate sales with CRM-based pipeline management and market-trend analysis, plus a site-engineering and retail-entrepreneurship background.",
  "skills": [
   "Sales & Negotiation",
   "Market Trend Analysis",
   "CRM Pipeline Management",
   "Excel Reporting",
   "Project Coordination",
   "Data Analysis (foundational)"
  ],
  "skill_marriage": "Combines real-estate sales, market analysis and site-engineering background with new data-science skills — suited to property-analytics, sales-data or market-research analyst roles.",
  "recommended_roles": [
   "Data Analyst (Real Estate / Market Research)",
   "Sales / Business Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Sales/market-analysis background; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "Real Estate"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Varghese George",
  "email": "varghese_george@live.com",
  "years_experience": "15+",
  "industry_background": "Civil engineering & construction project management",
  "prior_experience_summary": "Station Structure/Project Manager on major MRT construction (JRL), with an MS in Civil Engineering, managing schedules, quality control, stakeholders and procurement.",
  "skills": [
   "Project Management",
   "Construction / Civil Engineering",
   "Schedule & Quality Control",
   "Stakeholder Coordination",
   "Data Analysis (foundational)",
   "Reporting",
   "Procurement"
  ],
  "skill_marriage": "Combines senior construction project-management with new data-science skills — suited to project-analytics, construction-data or PMO-analyst roles where engineering domain plus analytics adds value.",
  "recommended_roles": [
   "Project / Construction Data Analyst",
   "PMO / Operations Analyst",
   "Business Analyst (Engineering)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior PM/engineer; data science is new, so pitch project-analytics/BA at senior-IC with domain depth.",
  "domain": "Engineering & Manufacturing"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Elaine Chong Yee Ting",
  "email": "ectt432@gmail.com",
  "years_experience": "15+",
  "industry_background": "Regional sales & account management (semiconductors, MICE)",
  "prior_experience_summary": "15+ years leading regional sales teams and key accounts across semiconductors (UTAC) and hospitality/MICE, with sales forecasting and tracking-system automation (Anaplan).",
  "skills": [
   "Regional Sales & Account Management",
   "Sales Forecasting (Anaplan)",
   "Team Leadership",
   "Data-Driven Sales Systems",
   "Stakeholder Management",
   "Data Analysis (foundational)",
   "Reporting"
  ],
  "skill_marriage": "Combines regional sales leadership and sales-forecasting/analytics-system experience with new data-science skills — suited to sales-analytics, forecasting-analyst or commercial business-analyst roles.",
  "recommended_roles": [
   "Sales / Commercial Analyst",
   "Forecasting / Demand Analyst",
   "Business Analyst (Sales)"
  ],
  "seniority": "Senior IC / Team-Lead potential",
  "seniority_note": "Senior sales leader with forecasting-systems exposure; as a data pivot, pitch sales-analytics at senior-IC.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Li Zhimin",
  "email": "zhimin25@gmail.com",
  "years_experience": "7+",
  "industry_background": "Accounting, finance & HR (multi-industry)",
  "prior_experience_summary": "5 years accounting/finance/admin plus 2.5 years HR across maritime, defence, healthcare and semiconductor sectors, with strong IT/data toolset (SQL, Python, Power BI, DAX).",
  "skills": [
   "Financial Reporting & Analytics",
   "SQL & Data Transformation",
   "Python (Analytics, ML basics)",
   "Power BI (DAX)",
   "Excel (Power Query)",
   "ERP (SAP, Oracle)",
   "Machine Learning (foundational)"
  ],
  "skill_marriage": "Combines finance/accounting and HR-operations experience with a genuinely strong self-built data toolset (SQL, Python, Power BI) — one of the more technically-ready DS profiles, suited to finance-analytics or data-analyst roles.",
  "recommended_roles": [
   "Data Analyst / Finance Data Analyst",
   "BI / Analytics Analyst",
   "Junior Data Scientist"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Solid finance base plus real data skills; mid-level data/finance-analytics roles are a genuine fit.",
  "domain": "Finance & Accounting"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Matthew Wong Yeang Tuck",
  "email": "matthewwong00075@gmail.com",
  "years_experience": "20+",
  "industry_background": "Social work & community/crisis care (public/social sector)",
  "prior_experience_summary": "20+ years in crisis response, community care and social services with a Social Work degree, doing coordinated assessments, case management and multidisciplinary collaboration, plus recent customer-service work.",
  "skills": [
   "Case Management & Assessment",
   "Crisis Response",
   "Stakeholder / Inter-Agency Coordination",
   "Documentation",
   "Customer Service",
   "Data Analysis (foundational)"
  ],
  "skill_marriage": "Combines social-work/case-management and public-service experience with new data-science skills — suited to social-sector analytics, programme-data or research/insights-analyst roles in healthcare/social services.",
  "recommended_roles": [
   "Data / Insights Analyst (Social / Healthcare)",
   "Programme / Research Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong social-sector background; data science is a big pivot, so entry-level analyst roles with domain relevance fit.",
  "domain": "Public Sector & Social"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Quek Kim Peng (Guo Jinbing)",
  "email": "quek_kp77@yahoo.com",
  "years_experience": "20+",
  "industry_background": "Software testing & QA engineering (electronics/transport)",
  "prior_experience_summary": "Principal Engineer at LTA and senior software test engineer roles, with an EEE degree, expert in test automation, Python/C++, and defect/root-cause analysis.",
  "skills": [
   "Software Testing & QA Automation",
   "Python / C++",
   "Test Frameworks (Selenium, Robot, JMeter)",
   "Root Cause Analysis",
   "Agile / SDLC",
   "Data Analysis (foundational)",
   "Machine Learning (foundational)"
  ],
  "skill_marriage": "Combines strong software-testing/engineering and programming background with new data-science skills — technically well-prepared, suited to data-analyst, test-data-analytics or junior data-engineer roles.",
  "recommended_roles": [
   "Data Analyst / Data Engineer",
   "QA / Test Data Analyst",
   "Junior Data Scientist"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Strong engineering/programming base; genuinely ready for mid-level technical data roles.",
  "domain": "Engineering & Manufacturing"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Tan Wah Kwai @ Jason Tan",
  "email": "jtwk108@gmail.com",
  "years_experience": "20+",
  "industry_background": "Industrial automation & aerospace maintenance",
  "prior_experience_summary": "20+ years in industrial automation engineering support and earlier aircraft maintenance, designing/installing automation systems and optimising machine performance for manufacturers.",
  "skills": [
   "Industrial Automation",
   "System Design & Integration",
   "Machine Optimisation",
   "Technical Troubleshooting",
   "Data Analysis (foundational)",
   "Machine Learning (foundational)"
  ],
  "skill_marriage": "Combines industrial-automation and engineering experience with new data-science skills — suited to manufacturing analytics, IoT/industrial-data or process-optimisation analyst roles bridging OT and data.",
  "recommended_roles": [
   "Data Analyst (Manufacturing / Industrial)",
   "Process / Automation Data Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong automation/engineering background; data science is new, so entry-to-mid industrial-analytics roles fit.",
  "domain": "Engineering & Manufacturing"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Tan Lay Choo, Beth",
  "email": "",
  "years_experience": "25+",
  "industry_background": "Accounting & finance (multi-industry)",
  "prior_experience_summary": "25+ years in accounting/finance (senior accounts executive, finance executive), handling full-set accounts, AR/AP, SAP, reconciliation, cash-flow forecasting and GST, ACCA-trained.",
  "skills": [
   "Full-Set Accounting",
   "AR / AP / GL",
   "ERP (SAP/EBS)",
   "Financial Reporting & Reconciliation",
   "Cash-Flow Forecasting",
   "Data Analysis (foundational)",
   "Excel"
  ],
  "skill_marriage": "Combines long accounting/finance and ERP experience with new data-science skills — suited to finance-analytics or reporting-analyst roles where accounting-data fluency strengthens the analysis.",
  "recommended_roles": [
   "Finance Data Analyst",
   "Reporting / Reconciliation Analyst",
   "Junior Data Analyst (Finance)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Very experienced in finance; data science is new, so pitch finance-analytics at senior-IC, not data-scientist.",
  "domain": "Finance & Accounting"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0526",
  "full_name": "Wan Marina Bt Wan Ishak",
  "email": "wantigerlady@gmail.com",
  "years_experience": "20+",
  "industry_background": "Client service & data/administration (healthcare, legal, aviation)",
  "prior_experience_summary": "20+ years in client service, office administration and data management across healthcare, legal and aviation, skilled in data entry, database management and enterprise systems (SAP, CRM, LIS, ERP).",
  "skills": [
   "Data & Database Management",
   "Client Service",
   "Enterprise Systems (SAP, CRM, LIS, ERP)",
   "Compliance Tracking",
   "Reporting",
   "Data Analysis (foundational)",
   "Excel"
  ],
  "skill_marriage": "Combines long data-management and client-service administration across regulated industries with new data-science skills — suited to data-management, data-quality or operations-analyst roles.",
  "recommended_roles": [
   "Data Management / Quality Analyst",
   "Operations / Reporting Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong data-admin background; data science is new, so entry-to-mid data/analyst roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0526",
  "full_name": "Christine Ho (Fong Yee Ho / He Fengyi)",
  "email": "christines@live.com.sg",
  "years_experience": "20+",
  "industry_background": "Human resources (MNC, hospitality, construction)",
  "prior_experience_summary": "IHRP-certified Senior HR Professional with 20+ years leading end-to-end HR operations, business partnering, C&B, HRIS implementation and policy governance across MNC, hospitality and construction.",
  "skills": [
   "HR Business Partnering",
   "HR Operations & C&B",
   "HRIS Implementation (SAP)",
   "Performance Management",
   "Policy Governance",
   "Digital Innovation Tools (foundational)",
   "Process Improvement"
  ],
  "skill_marriage": "Combines senior HR-operations and HRIS-implementation experience with new digital-innovation skills — suited to HR-tech, HR-digital-transformation or people-systems business-analyst roles.",
  "recommended_roles": [
   "HR Digital Transformation / HR-Tech Analyst",
   "Business Analyst (People Systems)",
   "HR Process Automation Executive"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior HR leader; digital-innovation is new, so pitch HR-tech/transformation at senior level.",
  "domain": "HR & Talent"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0526",
  "full_name": "Tan Kok Wee, Jansen (Chen Guowei)",
  "email": "jansen20@gmail.com",
  "years_experience": "20+",
  "industry_background": "Construction/project management & real estate investment",
  "prior_experience_summary": "Store Construction Manager at Nike managing stakeholders, vendors and budgets, with earlier regional investment/JV and business-development experience in real estate and construction.",
  "skills": [
   "Construction / Project Management",
   "Investment & JV Analysis",
   "Vendor & Stakeholder Management",
   "Budget Control",
   "Market Research",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines construction project-management and real-estate-investment experience with new digital-innovation skills — suited to project-digitalisation, operations-transformation or business-analyst roles in property/construction.",
  "recommended_roles": [
   "Project / Business Analyst (Construction / Real Estate)",
   "Digital Transformation Analyst",
   "Operations / PMO Analyst"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior PM/investment background; digital-innovation is new, so pitch analytics/BA at senior-IC.",
  "domain": "Project Management"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0526",
  "full_name": "Daniel Chen Junsheng",
  "email": "danielxav@gmail.com",
  "years_experience": "17+",
  "industry_background": "Marketing & content strategy (multi-sector)",
  "prior_experience_summary": "17 years in marketing communications and content/digital strategy across healthcare, banking, fintech and MICE, leading marketing strategy, campaigns and lead generation; also a PDPA practitioner.",
  "skills": [
   "Marketing & Content Strategy",
   "Digital Marketing Campaigns",
   "Product & Project Management",
   "Marketing Analytics",
   "Lead Generation",
   "Digital Innovation Tools (foundational)",
   "PDPA"
  ],
  "skill_marriage": "Combines marketing-strategy and content/digital experience with new digital-innovation skills — suited to marketing-technology, digital-product or marketing-transformation roles blending marketing with innovation tools.",
  "recommended_roles": [
   "MarTech / Digital Product Executive",
   "Digital Transformation (Marketing) Analyst",
   "Marketing Strategy / Content Lead"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior marketing professional; digital-innovation broadens toward MarTech/product — pitch at senior-IC.",
  "domain": "Marketing & Creative"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0526",
  "full_name": "Joseph Chia Hsiang Yang (Xie Xiangyang)",
  "email": "chiassy88@gmail.com",
  "years_experience": "20+",
  "industry_background": "Real estate investment & asset management",
  "prior_experience_summary": "~20 years in real-estate business development and investment/asset management across APAC (deal origination, financial modelling, due diligence, asset management), plus renewable-energy/data-centre investment, with a civil-engineering degree.",
  "skills": [
   "Investment & Asset Management",
   "Financial Modelling & Due Diligence",
   "Business Development",
   "Market Research",
   "Project Management",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines real-estate investment/asset-management and financial-modelling expertise with new digital-innovation skills — suited to proptech, investment-analytics or digital-transformation roles in real estate/infrastructure.",
  "recommended_roles": [
   "PropTech / Investment Analyst",
   "Business Analyst (Real Estate / Infrastructure)",
   "Digital Transformation Consultant"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior investment/asset-management professional; digital-innovation is new, so pitch analytics/transformation at senior level.",
  "domain": "Real Estate"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0526",
  "full_name": "Erming Ezekiel Lim Cokromulia",
  "email": "ermingezekiel@gmail.com",
  "years_experience": "20+",
  "industry_background": "Workplace safety & health / training (security, process plant)",
  "prior_experience_summary": "Experienced WSH professional and certified trainer/auditor (ISO 9001/14001/45001 lead auditor, ACTA/ACLP), with security and safety-management background across process plant and port facilities.",
  "skills": [
   "Workplace Safety & Health (WSH)",
   "ISO Auditing (9001/14001/45001)",
   "Training & Assessment (ACTA/ACLP)",
   "Risk Management",
   "Compliance",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines WSH, auditing and training expertise with new digital-innovation skills — suited to safety-digitalisation, compliance-tech or training-technology/transformation roles.",
  "recommended_roles": [
   "Safety / Compliance Digitalisation Analyst",
   "Learning Technology / Training Transformation Executive",
   "Business Analyst (WSH / Compliance)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior WSH/training professional; digital-innovation is new, so pitch domain-digitalisation at senior-IC.",
  "domain": "EHS & Safety"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0526",
  "full_name": "Erni Cokromulia",
  "email": "ernie_badz@yahoo.com",
  "years_experience": "15+",
  "industry_background": "Administration & operations (wholesale/food distribution)",
  "prior_experience_summary": "15+ years in a wholesale/food-distribution business, progressing from Sales Executive to Administrative Manager, overseeing administration, operations, team supervision and food-safety compliance.",
  "skills": [
   "Administrative & Operations Management",
   "Team Supervision",
   "Documentation & Reporting",
   "Customer Relations",
   "Compliance",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines administration/operations-management experience with new digital-innovation skills — suited to operations-digitalisation, process-improvement or business-analyst support roles in SME/distribution.",
  "recommended_roles": [
   "Operations / Process Analyst",
   "Business Analyst (Operations)",
   "Digital Transformation Support Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Ops/admin management background; digital-innovation is new, so mid-level ops/transformation roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0526",
  "full_name": "Galia Hong Chwee Woon",
  "email": "galia.hong@gmail.com",
  "years_experience": "20+",
  "industry_background": "Human resources & HR technology (regional)",
  "prior_experience_summary": "HR leader with 20+ years across Singapore, China and Taiwan, leading HR strategy, HRIS implementation, HR analytics (dashboards, KPIs), C&B and compliance.",
  "skills": [
   "HR Strategy & Business Partnering",
   "HRIS Implementation (SAP, ERP)",
   "HR Analytics & Dashboards",
   "Talent Management",
   "Compensation & Benefits",
   "Digital Innovation Tools (foundational)",
   "Change Management"
  ],
  "skill_marriage": "Combines senior regional HR and HRIS/HR-analytics experience with new digital-innovation skills — strong fit for HR-tech, HR-transformation or people-analytics business-analyst roles.",
  "recommended_roles": [
   "HR Digital Transformation / HR-Tech Analyst",
   "People Analytics / HRIS Business Analyst",
   "Digital Transformation Consultant (HR)"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior HR leader with HRIS/analytics depth; pitch HR-tech/transformation at senior level.",
  "domain": "HR & Talent"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0526",
  "full_name": "Muhammad Saat Bin Mat Ali",
  "email": "muhdsaat@gmail.com",
  "years_experience": "25+",
  "industry_background": "Real estate leadership, logistics & business management",
  "prior_experience_summary": "25+ years across real-estate division leadership (led ~150 agents), business/GM roles in cleaning & construction, and earlier SAF logistics supervision, focused on team leadership and operations.",
  "skills": [
   "Team Leadership & Mentoring",
   "Sales & Business Management",
   "Project Management",
   "Logistics / Operations",
   "Client Relations",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines large-team leadership, real-estate and operations-management experience with new digital-innovation skills — suited to operations-transformation, business-development or process-improvement roles.",
  "recommended_roles": [
   "Operations / Business Transformation Executive",
   "Business Development & Digital Executive",
   "Project / Operations Analyst"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior leader/manager; digital-innovation is new, so pitch transformation/ops roles leveraging leadership.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0526",
  "full_name": "Christine Tan Tsui Hsia (Chen Cuixia)",
  "email": "tsuihsia@gmail.com",
  "years_experience": "20+",
  "industry_background": "Supply chain & logistics (chemical, semicon, biopharma)",
  "prior_experience_summary": "Senior supply-chain professional across chemical, semiconductor and biopharma, leading planning, procurement, warehousing, logistics, 3PL strategy and sustainability, with SMU sustainability certification.",
  "skills": [
   "Supply Chain Strategy",
   "Procurement & Logistics",
   "3PL & Network Optimisation",
   "Sustainability",
   "Operational Excellence",
   "Digital Innovation Tools (foundational)",
   "Data-Driven Optimisation"
  ],
  "skill_marriage": "Combines senior supply-chain strategy and optimisation experience with new digital-innovation skills — suited to supply-chain-digitalisation, operations-transformation or business-analyst roles in logistics/manufacturing.",
  "recommended_roles": [
   "Supply Chain Digital Transformation Analyst",
   "Operations / Business Analyst (Supply Chain)",
   "Digital Transformation Consultant"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior supply-chain leader; digital-innovation is new, so pitch transformation/analytics at senior level.",
  "domain": "Supply Chain & Procurement"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0526",
  "full_name": "Steven Tran Thu Van",
  "email": "nihonsteven@hotmail.com",
  "years_experience": "15+",
  "industry_background": "Learning & development / organisational development (global tech)",
  "prior_experience_summary": "Global L&D leader with 15+ years designing and scaling learning academies at TikTok, Expedia, Apple and others, with AI-enabled learning design and strengths-based coaching.",
  "skills": [
   "Learning & Development Strategy",
   "Organisational Development",
   "AI-Enabled Learning Design",
   "Facilitation & Coaching",
   "Capability Frameworks",
   "Digital Innovation Tools (foundational)",
   "Vendor Management"
  ],
  "skill_marriage": "Combines global L&D/OD leadership and AI-enabled learning design with new digital-innovation skills — suited to learning-technology, digital-capability or people-development-transformation roles.",
  "recommended_roles": [
   "Learning Technology / Digital L&D Lead",
   "Capability / Transformation Consultant",
   "Business Analyst (People Development)"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior global L&D leader; digital-innovation extends toward learning-tech — pitch at senior level.",
  "domain": "HR & Talent"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0526",
  "full_name": "Zhang QingFeng, Jack",
  "email": "jackqfzhang@gmail.com",
  "years_experience": "30",
  "industry_background": "Software & embedded/IoT engineering",
  "prior_experience_summary": "30 years in IT and electronics development, currently senior software engineer focused on embedded/IoT products (C++, C#, Python, .NET, Java), including robotics and hardware/PCB troubleshooting.",
  "skills": [
   "Software Engineering (C++, C#, Python)",
   "Embedded / IoT Development",
   "Robotics (ROS2)",
   "Firmware Development",
   "Hardware / PCB Troubleshooting",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines deep software/embedded-engineering experience with new digital-innovation skills — suited to IoT/embedded-solutions, digital-product-development or technical-innovation roles.",
  "recommended_roles": [
   "IoT / Embedded Solutions Developer",
   "Digital Product / Technical Innovation Engineer",
   "Application Developer"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Very experienced engineer; digital-innovation complements strong technical depth — pitch technical roles at senior-IC.",
  "domain": "IT & Infrastructure"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0526",
  "full_name": "Benedict Boo Yong Wah (Wu Ronghua)",
  "email": "ywboo2@gmail.com",
  "years_experience": "10+",
  "industry_background": "Finance & accounting (multi-industry MNC/GLC)",
  "prior_experience_summary": "Chartered Accountant with 10+ years in financial/cost accounting, treasury, consolidation and finance systems implementation (SAP, Blackline, Alteryx, Tableau), including IFRS 17 and post-M&A integration.",
  "skills": [
   "Financial & Cost Accounting",
   "Finance Systems (SAP, Blackline, Alteryx, Tableau)",
   "Group Consolidation",
   "Process Improvement",
   "Project Management",
   "Digital Innovation Tools (foundational)",
   "Internal Controls"
  ],
  "skill_marriage": "Combines chartered-accountant finance expertise and finance-systems implementation with new digital-innovation skills — strong fit for finance-transformation, finance-automation or finance-systems business-analyst roles.",
  "recommended_roles": [
   "Finance Transformation / Systems Analyst",
   "Business Analyst (Finance Systems)",
   "Finance Automation / Digitalisation Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Strong CA with systems-implementation track record; genuinely ready for finance-transformation/BA roles at senior-IC.",
  "domain": "Finance & Accounting"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Jason Chia Hee Peng",
  "email": "",
  "years_experience": "25+",
  "industry_background": "Creative / art direction & brand design (advertising)",
  "prior_experience_summary": "Long-serving Art Director across multiple agencies (Greative, Flash Communications, Royalworkz), leading creative concept development and campaigns for major brands (Prudential, Shell, Unilever, TikTok).",
  "skills": [
   "Art Direction & Creative Concept",
   "Brand Development",
   "Campaign Design (Print, Web, Interactive)",
   "Client & Stakeholder Engagement",
   "Content Creation",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines decades of agency art-direction and brand-campaign experience with new digital-marketing skills — can both create the creative and run the campaigns, ideal for content-led or creative marketing roles.",
  "recommended_roles": [
   "Content / Creative Marketing Lead",
   "Brand & Campaign Marketing Executive",
   "Social Media & Creative Marketing Executive"
  ],
  "seniority": "Senior IC / Team-Lead potential",
  "seniority_note": "Very senior creative; digital-marketing formalises a strong creative base — pitch content/creative lead, not entry-level.",
  "domain": "Marketing & Creative"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "John Lee Sze Hian (Li Shixian)",
  "email": "shleesx13@gmail.com",
  "years_experience": "15+",
  "industry_background": "Real estate sales, coaching & telecom field work",
  "prior_experience_summary": "Varied career spanning real-estate sales management, bowling coaching/equipment sales, and current telecom field network-testing and customer advisory.",
  "skills": [
   "Sales & Customer Advisory",
   "Real Estate Sales",
   "Coaching / Training",
   "Field Assessment",
   "Customer Service",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines sales, coaching and customer-advisory experience with new digital-marketing skills — suited to entry-level marketing, sales-support or customer-engagement roles.",
  "recommended_roles": [
   "Digital Marketing Executive (SME)",
   "Sales & Marketing Support Executive",
   "Customer Engagement / Marketing Coordinator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Varied non-marketing background; marketing is a fresh pivot, so entry-level roles fit best.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Susan Lim",
  "email": "",
  "years_experience": "25+",
  "industry_background": "Risk, compliance & wealth management (private banking)",
  "prior_experience_summary": "CFA/FRM-qualified senior risk and compliance leader (Head of Risk Asia at Lombard Odier, Director at UBS), implementing risk frameworks, investment suitability and governance in private banking.",
  "skills": [
   "Risk Management & Governance",
   "Compliance (AML, Investment Suitability)",
   "Financial Analysis",
   "Regulatory Frameworks",
   "Stakeholder Communication",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines senior risk/compliance and financial expertise with new digital-marketing skills — suited to compliance-aware marketing, financial-services content marketing or marketing roles in regulated wealth/banking settings.",
  "recommended_roles": [
   "Marketing Executive (Financial Services / Compliance-aware)",
   "Content Marketing (Wealth / Banking)",
   "Marketing & Communications Executive"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Very senior in risk/compliance; marketing is a significant pivot — best in finance-sector marketing leveraging domain credibility, not creative/entry roles.",
  "domain": "Banking & Wealth"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Nurul Yaqin Binte Tahar",
  "email": "nurul.tahar@live.com",
  "years_experience": "10+",
  "industry_background": "Customer service (health, insurance, banking)",
  "prior_experience_summary": "10+ years in customer-service and relationship roles across health insurance, hospitality and banking (DBS, Raffles Health Insurance), skilled in CRM, complaint resolution and customer retention.",
  "skills": [
   "Customer Service & Retention",
   "CRM Systems",
   "Complaint Resolution",
   "Client Communication",
   "Time Management",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines strong customer-service and CRM experience with new digital-marketing skills — suited to CRM marketing, customer-engagement or marketing-support roles where customer understanding drives retention.",
  "recommended_roles": [
   "CRM / Customer Marketing Executive",
   "Digital Marketing Coordinator",
   "Customer Engagement Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Service/CRM background; marketing is new, so entry-to-mid marketing roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Chia Wee Kwang",
  "email": "m7chia@yahoo.com.sg",
  "years_experience": "25+",
  "industry_background": "Technical/industrial sales & operations (machine tools)",
  "prior_experience_summary": "25+ years in industrial machine-tool sales and operations at Makino and GF Machining, driving revenue growth, market analysis, sales presentations and territory planning.",
  "skills": [
   "Technical / Industrial B2B Sales",
   "Sales Strategy & Prospecting",
   "Market Analysis",
   "Customer Relationship Management",
   "Sales Presentations",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines long industrial-sales and market-analysis experience with new digital-marketing skills — suited to B2B/industrial marketing, product-marketing or channel-marketing roles.",
  "recommended_roles": [
   "B2B / Industrial Marketing Executive",
   "Product / Sales Marketing Executive",
   "Digital Marketing Executive (Technical)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior industrial-sales professional; marketing is new, so pitch B2B/technical marketing at senior-IC.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Gerald Chiang Jie Xiong (Zhang Jiexiong)",
  "email": "Neojxg@gmail.com",
  "years_experience": "12+",
  "industry_background": "Financial trading, dealing & sales/marketing analysis",
  "prior_experience_summary": "Equity/forex dealer and trader across KGI, ANZ and CIMB, more recently doing sales and marketing data analysis at Parkway Shenton, with CRM and pivot-table reporting.",
  "skills": [
   "Sales & Marketing Data Analysis",
   "CRM Systems",
   "Financial Markets / Trading",
   "Excel (Pivot Tables)",
   "Reporting",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines financial-trading and sales/marketing-analysis experience with new digital-marketing skills — suited to marketing-analytics, CRM or data-leaning marketing roles.",
  "recommended_roles": [
   "Marketing Analytics / CRM Executive",
   "Digital Marketing Executive (Data-leaning)",
   "Marketing Operations Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Trading/analysis background; marketing is new, so mid-level analytical marketing roles fit.",
  "domain": "Banking & Wealth"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Sabrina Chong Mun Teng",
  "email": "sabrinacmt@gmail.com",
  "years_experience": "15+",
  "industry_background": "Office management & administration (fintech, engineering, oil trading)",
  "prior_experience_summary": "15+ years as Office Manager / Senior Admin Executive across fintech, engineering consulting and oil trading, managing office operations, vendors, budgets, HR support and regional coordination.",
  "skills": [
   "Office & Facilities Management",
   "Vendor & Budget Management",
   "Administrative Operations",
   "HR / Recruitment Support",
   "Event Coordination",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines long office-management and administration experience with new digital-marketing skills — suited to marketing-operations, marketing-admin or event-coordination roles.",
  "recommended_roles": [
   "Marketing Operations / Admin Executive",
   "Event Marketing Coordinator",
   "Marketing Support Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Admin/ops background; marketing is a fresh pivot, so entry-to-mid marketing-ops roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Ho Hui Ling (He Huiling)",
  "email": "mary_ho0921@yahoo.com.sg",
  "years_experience": "12+",
  "industry_background": "Venue & event sales (MICE industry)",
  "prior_experience_summary": "12+ years as Sales Manager at Suntec Convention Centre in MICE venue sales, managing 300+ events annually and ~S$2.5M revenue through business development, account management and contract negotiation.",
  "skills": [
   "Event & Venue Sales",
   "Business Development",
   "Account Management",
   "Contract Negotiation",
   "Client Relationship Management",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines strong MICE venue-sales and account-management experience with new digital-marketing skills — suited to event marketing, hospitality/venue marketing or B2B marketing roles.",
  "recommended_roles": [
   "Event / MICE Marketing Executive",
   "B2B / Account-Based Marketing Executive",
   "Business Development & Marketing Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior in event/venue sales; marketing is new, so pitch event/B2B marketing at senior-IC.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Ernest Lim Chen Seng (Lim ZhenXing, Ernest)",
  "email": "",
  "years_experience": "15+",
  "industry_background": "Real estate sales & marketing",
  "prior_experience_summary": "15+ years in real estate as a Senior Marketing Director and top-producer, handling residential resale, commercial and new-launch marketing, client relationships and property investment advisory.",
  "skills": [
   "Property Marketing & Sales",
   "New Launch Campaigns",
   "Client Relationship Management",
   "Negotiation",
   "Market Knowledge",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines long real-estate marketing/sales and new-launch campaign experience with formal digital-marketing skills — a natural fit for real-estate, property-tech or lead-generation marketing roles.",
  "recommended_roles": [
   "Digital Marketing Executive (Real Estate / PropTech)",
   "Property Marketing & Lead Gen Executive",
   "Campaign Marketing Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior property-sales/marketing producer; formal marketing skills round it out — mid-to-senior marketing roles fit.",
  "domain": "Real Estate"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Mok Wai Yin (Mo Huixian)",
  "email": "dieselmok4@hotmail.com",
  "years_experience": "10+",
  "industry_background": "F&B & retail multi-store operations",
  "prior_experience_summary": "10+ years with Starbucks Singapore rising to District Manager, leading multi-store operations, team development, P&L, cost control and customer-experience across stores.",
  "skills": [
   "Multi-Store Operations",
   "Team Leadership & Development",
   "Sales Growth Strategy",
   "P&L / Budget Control",
   "Customer Experience",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines multi-store retail/F&B operations leadership with new digital-marketing skills — suited to retail marketing, customer-experience marketing or brand-operations roles.",
  "recommended_roles": [
   "Retail / Brand Marketing Executive",
   "Customer Experience Marketing Executive",
   "Marketing Operations Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior retail-ops manager; marketing is new, so pitch retail/brand marketing at senior-IC.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Karthiaini D/O Sumangan",
  "email": "karthiaini84@gmail.com",
  "years_experience": "7+",
  "industry_background": "Finance & accounting (general ledger operations)",
  "prior_experience_summary": "Finance Executive at Evo Outsourcing/UOB handling general-ledger operations, reconciliations, controls, audit support and RPA-improvement projects, with an Accountancy degree.",
  "skills": [
   "General Ledger & Finance Operations",
   "Reconciliation & Controls",
   "Data Analysis (GL)",
   "RPA / Process Improvement",
   "Documentation",
   "Excel",
   "Power BI (foundational)"
  ],
  "skill_marriage": "Combines finance/GL-operations and process-improvement experience with new data-science skills — suited to finance-analytics or reporting-analyst roles where accounting-data fluency strengthens the analysis.",
  "recommended_roles": [
   "Finance Data Analyst",
   "Reporting / Reconciliation Analyst",
   "Junior Data Analyst (Finance)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Solid finance background; data science is new, so entry-to-mid finance-analytics roles fit.",
  "domain": "Finance & Accounting"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Low Hwee Min, Gillian (Liu Huimin)",
  "email": "zgil29@gmail.com",
  "years_experience": "15+",
  "industry_background": "Healthcare patient services & operations",
  "prior_experience_summary": "15+ years in healthcare patient services at SingHealth, leading frontline teams, coordinating operations and analysing patient-service data (Excel VLOOKUP/pivot, KPI dashboards) for process improvement.",
  "skills": [
   "Operations Coordination",
   "Data Analysis & KPI Reporting",
   "Advanced Excel (VLOOKUP, Pivot)",
   "Oracle & SAP",
   "Team Leadership",
   "Dashboard Reporting",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines healthcare operations-coordination and hands-on service-data analysis with new data-science skills — suited to healthcare/operations analytics or reporting-analyst roles.",
  "recommended_roles": [
   "Operations / Healthcare Data Analyst",
   "Reporting / KPI Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Operations/data-reporting background; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Jacqueline Liew Mee Kuah",
  "email": "jacliew18@gmail.com",
  "years_experience": "20+",
  "industry_background": "Procurement & supply chain (multinational)",
  "prior_experience_summary": "20+ years in procurement, inventory planning and logistics, more recently order management and customer operations at Laerdal, with ERP systems (QAD, Oracle, SAP) and Power BI exposure.",
  "skills": [
   "Procurement & Supply Chain",
   "Order Management & Fulfilment",
   "Inventory Planning",
   "ERP (QAD, Oracle, SAP)",
   "Data Analysis (Excel, Power BI)",
   "Logistics Coordination"
  ],
  "skill_marriage": "Combines long procurement/supply-chain and ERP-data experience with new data-science skills — suited to supply-chain-analytics, procurement-data or operations-analyst roles.",
  "recommended_roles": [
   "Supply Chain / Procurement Data Analyst",
   "Operations / Business Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong supply-chain background; data science is new, so entry-to-mid analytics roles fit.",
  "domain": "Supply Chain & Procurement"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Soe Win Htut",
  "email": "swhtut@yahoo.com",
  "years_experience": "20+",
  "industry_background": "Mechanical / infrastructure engineering (water, environmental)",
  "prior_experience_summary": "Engineering Manager with 20+ years delivering infrastructure/water/MEICA engineering projects (PUB), with MSc Mechanical, project lifecycle leadership, and recent GenAI/data-driven decision-support training.",
  "skills": [
   "Mechanical / MEICA Engineering",
   "Project & Construction Management",
   "Engineering Data Interpretation",
   "Data-Driven Decision Support",
   "Cost Optimisation",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines senior engineering project-management and engineering-data experience with new data-science skills — suited to engineering-analytics, infrastructure-data or project-analytics roles.",
  "recommended_roles": [
   "Data Analyst (Engineering / Infrastructure)",
   "Project / Operations Analyst",
   "Business Analyst (Engineering)"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Very senior engineer/manager; data science is new, so pitch engineering-analytics at senior level with domain depth.",
  "domain": "Engineering & Manufacturing"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Cheng ZhiXian (Zhong ZhiXian)",
  "email": "zhixian@gmail.com",
  "years_experience": "8+",
  "industry_background": "Financial services advisory & sales",
  "prior_experience_summary": "Financial Services Consultant building client relationships and driving sales, with financial modelling, data analysis, investment strategy and risk-management understanding.",
  "skills": [
   "Financial Advisory & Sales",
   "Financial Modelling",
   "Data Analysis",
   "Investment Strategy",
   "Client Relationship Management",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines financial-advisory and financial-modelling experience with new data-science skills — suited to finance-analytics, investment-data or business-analyst roles in financial services.",
  "recommended_roles": [
   "Finance / Investment Data Analyst",
   "Business Analyst (Financial Services)",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Financial-advisory background; data science is new, so entry-to-mid finance-analytics roles fit.",
  "domain": "Banking & Wealth"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Daphne Gwee",
  "email": "daphnegwee@yahoo.com.sg",
  "years_experience": "10+",
  "industry_background": "Telecom project coordination & operations",
  "prior_experience_summary": "10+ years at Nokia in project coordination and acceptance, tracking site readiness, documentation, POs and running data analysis to align Master Dashboard and Power BI reports.",
  "skills": [
   "Project Coordination",
   "Data Analysis & Dashboard Alignment",
   "Power BI",
   "Documentation & Compliance",
   "Stakeholder Collaboration",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines telecom project-coordination and data/dashboard-reporting experience with new data-science skills — suited to project-analytics, operations-data or reporting-analyst roles.",
  "recommended_roles": [
   "Project / Operations Data Analyst",
   "Reporting / BI Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Coordination/reporting background; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Foong Hak Chung, Brian (Feng Kechong)",
  "email": "brifoongan@yahoo.com",
  "years_experience": "20+",
  "industry_background": "Arts, gallery & creative sector (curation/management)",
  "prior_experience_summary": "20+ years as gallery director, curator and creative entrepreneur (iPreciation, Art Galleries Association Singapore), managing exhibitions, sales data, collector relations and operations.",
  "skills": [
   "Gallery & Arts Management",
   "Curation & Exhibition Planning",
   "Sales & Collector Data",
   "Stakeholder Coordination",
   "Marketing & Programmes",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines arts/gallery management and sales-data experience with new data-science skills — suited to arts-tech, cultural-data or audience-analytics roles bridging creative sector and data.",
  "recommended_roles": [
   "Data / Insights Analyst (Arts / Culture)",
   "Audience / CRM Data Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior arts-sector leader; data science is a big pivot, so pitch data/audience-analytics with domain relevance, entry-to-mid.",
  "domain": "Marketing & Creative"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Eyvone Ho Xiao Fen (He Xiaofen)",
  "email": "hoeyvone@hotmail.com",
  "years_experience": "10+",
  "industry_background": "Banking operations & compliance (private banking)",
  "prior_experience_summary": "Banking professional at UBS in process/quality and front-office integration roles, handling client lifecycle, KYC/AML compliance and process improvement, now building data analytics skills.",
  "skills": [
   "Banking Operations",
   "KYC / AML Compliance",
   "Process Improvement",
   "Client Lifecycle Management",
   "Data Analysis (foundational)",
   "Business Intelligence (foundational)"
  ],
  "skill_marriage": "Combines banking-operations and compliance experience with new data-science skills — suited to banking-analytics, compliance-data or operations-analyst roles in financial services.",
  "recommended_roles": [
   "Data Analyst (Banking / Compliance)",
   "Operations / Process Analyst",
   "Business Analyst (Financial Services)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Banking-ops/compliance background; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "Banking & Wealth"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Jayapriya Ragin Drann",
  "email": "priyaragin07@gmail.com",
  "years_experience": "20+",
  "industry_background": "Operations & administration (publishing, digital services)",
  "prior_experience_summary": "20+ years in operations, administration and stakeholder management across publishing and digital services, handling workflows, reporting, CRM (Salesforce), events and team coordination.",
  "skills": [
   "Operations & Admin Management",
   "CRM & Database Management",
   "Data Analysis & Reporting",
   "Team Coordination",
   "Process Improvement",
   "Salesforce / JIRA",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines long operations/administration and CRM-data experience with new data-science skills — suited to operations-analytics, CRM-data or reporting-analyst roles.",
  "recommended_roles": [
   "Operations / Business Data Analyst",
   "CRM / Reporting Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Ops/admin background; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Lin Hanqiang",
  "email": "hanq@hotmail.sg",
  "years_experience": "15+",
  "industry_background": "Workplace safety & health, IT & business (multi-domain)",
  "prior_experience_summary": "MBA-qualified professional with a varied background spanning naval service, HSE/workplace-safety management, IT administration and data-governance/blockchain certificates.",
  "skills": [
   "Workplace Safety & Health",
   "IT Administration",
   "Data Governance",
   "Business Management",
   "Advanced Excel",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines WSH, IT-administration and business/data-governance background with new data-science skills — suited to safety-analytics, governance-data or operations-analyst roles.",
  "recommended_roles": [
   "Data / Governance Analyst",
   "Safety / Operations Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Varied WSH/IT/business background; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "EHS & Safety"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Ray Wong Swee Hon",
  "email": "cosmoray77@gmail.com",
  "years_experience": "14+",
  "industry_background": "ICT/telecom account management & sales",
  "prior_experience_summary": "14+ years in ICT/telecom account management and sales, with corporate account management, client needs analysis and CRM (Salesforce), plus recent admin/operations and level-1 IT support.",
  "skills": [
   "ICT Solutions Sales",
   "Key Account Management",
   "CRM (Salesforce)",
   "Client Needs Analysis",
   "Data Analysis (foundational)",
   "Excel",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines ICT/telecom account-management and sales-data experience with new data-science skills — suited to sales-analytics, commercial-data or business-analyst roles.",
  "recommended_roles": [
   "Sales / Commercial Data Analyst",
   "Business Analyst (ICT)",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Sales/account-management background; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Sugandha Taneja",
  "email": "dudeja.sugandha@gmail.com",
  "years_experience": "6+",
  "industry_background": "Early childhood education & learner-data operations",
  "prior_experience_summary": "ECDA-registered early-childhood educator running a daily learner-data system (Qoqolo) for 28 students, owning assessments, reporting, ECDA audits, with a Masters in Mathematics and SQL/RDBMS foundations.",
  "skills": [
   "Learner Data Management",
   "Reporting & Documentation",
   "SQL / RDBMS (foundational)",
   "Assessment & Analysis",
   "Compliance / Audit",
   "Mathematics",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines education/learner-data operations and a strong mathematics/SQL foundation with new data-science skills — suited to education-data, reporting-analyst or junior data-analyst roles.",
  "recommended_roles": [
   "Data Analyst (Education / Reporting)",
   "Junior Data Analyst",
   "Business / Insights Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Maths degree and SQL foundation help; data science is newly formalised, so entry-level analyst roles fit.",
  "domain": "Education & Training"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Sulaiman Bin Ismail",
  "email": "sulaiman8623@gmail.com",
  "years_experience": "20+",
  "industry_background": "Information security & SOC operations (cybersecurity)",
  "prior_experience_summary": "Information Security Analyst with two decades across security operations, access management and risk governance, now in a global SOC doing threat detection and incident response, with multiple cybersecurity certifications.",
  "skills": [
   "Security Operations (SOC)",
   "Threat Detection & Incident Response",
   "Risk & Compliance",
   "Access Management",
   "Data Analysis (foundational)",
   "Detection Engineering (learning)",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines deep security-operations/SOC experience with new data-science skills — suited to security-analytics, threat-data or SOC-data-analyst roles where cyber domain plus data adds value.",
  "recommended_roles": [
   "Security / SOC Data Analyst",
   "Threat / Risk Analyst",
   "Data Analyst (Cybersecurity)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior security professional; data science complements a strong cyber base — pitch security-analytics at senior-IC.",
  "domain": "IT & Infrastructure"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Yenmalachintala Anitha",
  "email": "",
  "years_experience": "4+",
  "industry_background": "IT service desk & cloud support",
  "prior_experience_summary": "IT professional with 4 years in service-desk support for cloud environments at Synapxe, using ServiceNow/JIRA, ITIL processes, ticket automation and incident management, aiming toward system-analyst work.",
  "skills": [
   "Cloud Support & Troubleshooting",
   "IT Service Management (ServiceNow, ITIL)",
   "Incident & Problem Management",
   "JIRA / Confluence",
   "Automation",
   "Data Analysis (foundational)",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines IT service-desk/cloud-support experience with new data-science skills — suited to IT-data, service-analytics or junior data/systems-analyst roles.",
  "recommended_roles": [
   "Data / Systems Analyst (IT)",
   "Service / Operations Data Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Early-career IT-support background; data science is new, so entry-level analyst roles fit.",
  "domain": "IT & Infrastructure"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Acacia-Aoki Liang (Long Yu Xin)",
  "email": "acacia.aoki@gmail.com",
  "years_experience": "15+",
  "industry_background": "Operations, business development & facilities (healthcare, pharma)",
  "prior_experience_summary": "15+ years across facilities management, pharmaceutical sales and healthcare operations, handling client acquisition, contract/vendor management and revenue growth.",
  "skills": [
   "Operations & Facilities Management",
   "Business Development",
   "Contract & Vendor Negotiation",
   "Client Relationship Management",
   "KPI Monitoring",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines operations, business-development and facilities experience with new digital-innovation skills — suited to operations-digitalisation, business-analyst or transformation-support roles.",
  "recommended_roles": [
   "Operations / Business Analyst",
   "Digital Transformation Support Executive",
   "Process Improvement Analyst"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior ops/BD background; digital-innovation is new, so pitch analytics/transformation at senior-IC.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Nuraini Binte Ahmad",
  "email": "nbertauhid@gmail.com",
  "years_experience": "15+",
  "industry_background": "Education, training & AI language annotation",
  "prior_experience_summary": "Early-childhood/education trainer (Shichida Method) now doing AI language quality review and annotation, evaluating LLM outputs for accuracy, coherence and safety in English and Malay.",
  "skills": [
   "Education & Training",
   "AI Data Annotation / LLM Evaluation",
   "Linguistic Quality Review",
   "Analytical Reasoning",
   "Attention to Detail",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines education/training and hands-on AI-annotation/LLM-evaluation experience with new digital-innovation skills — suited to AI-data, content-quality or digital-education roles.",
  "recommended_roles": [
   "AI Data / Content Quality Analyst",
   "Digital Learning / EdTech Executive",
   "Business Analyst (AI / Content)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Education plus AI-annotation background; digital-innovation is new, so entry-to-mid roles fit.",
  "domain": "Education & Training"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Ryan Lio Ann Haur (Liang Anhao)",
  "email": "ryan.lio.fwd@gmail.com",
  "years_experience": "20+",
  "industry_background": "IoT solutions & manufacturing technology (leadership)",
  "prior_experience_summary": "20+ years managing manufacturing-IoT solutions and technology consulting, leading cross-functional teams to design and scale IoT platforms for real-time monitoring and data-driven decisions.",
  "skills": [
   "IoT Solutions & Architecture",
   "Manufacturing Technology",
   "Cross-functional Team Leadership",
   "Technology Roadmapping",
   "Vendor / Partner Management",
   "Digital Innovation Tools",
   "Data-Driven Decision Making"
  ],
  "skill_marriage": "Combines senior IoT/manufacturing-technology leadership with new digital-innovation skills — strong fit for digital-transformation, IoT-solutions or Industry-4.0 innovation roles.",
  "recommended_roles": [
   "Digital Transformation / IoT Solutions Lead",
   "Digital Innovation Manager",
   "Business Analyst (Manufacturing Tech)"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior IoT/tech leader; digital-innovation complements strongly — pitch transformation/innovation at senior level.",
  "domain": "IT & Infrastructure"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Yoong Siew Tee",
  "email": "yoongst@gmail.com",
  "years_experience": "20+",
  "industry_background": "Quality management & operational excellence (semiconductor)",
  "prior_experience_summary": "20+ years in quality management at GlobalFoundries, driving systematic improvement, data-driven problem solving (FMEA, DMAIC, SPC) and cross-functional quality programs for high-value accounts.",
  "skills": [
   "Quality Management",
   "Statistical Process Control (SPC)",
   "Data-Driven Problem Solving (FMEA, DMAIC)",
   "Process Improvement",
   "Cross-functional Leadership",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines quality-management and data-driven-improvement experience with new digital-innovation skills — suited to quality-analytics, process-digitalisation or operational-excellence transformation roles.",
  "recommended_roles": [
   "Quality / Process Data Analyst",
   "Operational Excellence / Transformation Analyst",
   "Business Analyst (Manufacturing)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior quality professional with strong data-tools; digital-innovation is new, so pitch quality-analytics/transformation at senior-IC.",
  "domain": "Engineering & Manufacturing"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Boo Boon Chia (Wu Wenzheng)",
  "email": "ek3bbc@yahoo.com",
  "years_experience": "28+",
  "industry_background": "Workplace safety, facility & fire safety management (aerospace)",
  "prior_experience_summary": "28+ years in WSH, facility and fire-safety management across aerospace maintenance and engineering operations, with risk assessment, safety audits, incident investigation and contractor management.",
  "skills": [
   "Workplace Safety & Health (WSH)",
   "Facility & Fire Safety Management",
   "Risk Assessment & Audits",
   "Incident Investigation",
   "Contractor Management",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines long WSH/facility/fire-safety experience with new digital-innovation skills — suited to safety-digitalisation, compliance-tech or facilities-transformation roles.",
  "recommended_roles": [
   "Safety / Facilities Digitalisation Analyst",
   "Compliance / Process Transformation Executive",
   "Business Analyst (WSH / Facilities)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Very experienced WSH/facilities professional; digital-innovation is new, so pitch domain-digitalisation at senior-IC.",
  "domain": "EHS & Safety"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Chris Louisa Ng Chay Luang",
  "email": "clouisa_64@hotmail.com",
  "years_experience": "27+",
  "industry_background": "Executive administration & corporate governance (multi-sector)",
  "prior_experience_summary": "27+ years as Executive Assistant supporting C-suite across finance, healthcare, energy, shipping, IT/AI and education, with executive administration, governance, procurement and event management.",
  "skills": [
   "Executive Administration",
   "Corporate Governance",
   "Calendar & Travel Management",
   "Procurement",
   "Event Management",
   "Digital Workplace Tools",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines long executive-administration and governance experience with new digital-innovation skills — suited to operations-digitalisation, administrative-transformation or business-support-analyst roles.",
  "recommended_roles": [
   "Operations / Admin Transformation Executive",
   "Business Support / Process Analyst",
   "Digital Workplace Coordinator"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Very experienced EA; digital-innovation is new, so entry-to-mid transformation/ops roles leveraging admin depth fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Michelle Leia",
  "email": "michsiah@yahoo.com.sg",
  "years_experience": "15+",
  "industry_background": "Executive administration (FMCG, banking)",
  "prior_experience_summary": "Executive Assistant supporting C-suite at Unilever and ANZ, handling calendar/travel/expenses, budget reports, vendor setup, event support and team coordination.",
  "skills": [
   "Executive Administration",
   "Calendar & Travel Management",
   "Budget Reporting",
   "Vendor & PO Management",
   "Event Coordination",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines executive-administration and coordination experience with new digital-innovation skills — suited to operations-support, administrative-digitalisation or business-coordination roles.",
  "recommended_roles": [
   "Operations / Admin Support Executive",
   "Business Coordination / Process Executive",
   "Digital Workplace Coordinator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Strong EA background; digital-innovation is new, so entry-to-mid ops/admin roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Nur Eliza Bte Md Yussof",
  "email": "elyza26isabel@gmail.com",
  "years_experience": "10+",
  "industry_background": "HR (L&D), workplace safety & operations",
  "prior_experience_summary": "10+ years in management across HR learning & development, workplace safety and operations, designing training programs, leading teams, with recent cybersecurity/IT training.",
  "skills": [
   "HR / Learning & Development",
   "Workplace Safety",
   "Operations Management",
   "Training Design",
   "IT / Cybersecurity (foundational)",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines HR/L&D, safety and operations-management experience with new digital-innovation and IT skills — suited to HR-tech, learning-technology or operations-transformation roles.",
  "recommended_roles": [
   "HR-Tech / Learning Technology Executive",
   "Operations / Process Transformation Analyst",
   "Business Analyst (People / Operations)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "HR/L&D/ops background; digital-innovation is new, so mid-level HR-tech/transformation roles fit.",
  "domain": "HR & Talent"
 },
 {
  "specialist": "Jim",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Terry Foo Tiang Hong (Fu Xianghong)",
  "email": "terryfoo@gmail.com",
  "years_experience": "20+",
  "industry_background": "Financial sales, business development & talent acquisition (insurance/banking)",
  "prior_experience_summary": "20+ years in financial sales, business development, channel/partner management and talent acquisition across insurance and banking (AIA, Singlife), building partnerships and driving sales.",
  "skills": [
   "Business Development & Channel Management",
   "Financial Sales",
   "Talent Acquisition",
   "Partnership Building",
   "Training & Coaching",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines financial-sales, business-development and partnership experience with new digital-innovation skills — suited to digital-partnership, business-development or transformation roles in financial services.",
  "recommended_roles": [
   "Business Development / Partnership Executive (Digital)",
   "Digital Transformation Analyst (Financial Services)",
   "Business Analyst (Sales / Partnerships)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior BD/sales professional; digital-innovation is new, so pitch digital-BD/transformation at senior-IC.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Fong Soo San (Susan)",
  "email": "ssfong@singnet.com.sg",
  "years_experience": "20+",
  "industry_background": "Global operations & customer experience (travel, e-commerce)",
  "prior_experience_summary": "20+ years leading multinational operations and customer-experience teams across travel and e-commerce (Amazon), driving SLA/KPI performance, process optimisation and team leadership of 50+ staff.",
  "skills": [
   "Global Operations Management",
   "Customer Experience",
   "SLA / KPI Optimisation",
   "Process Improvement & Automation",
   "Team Leadership",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines large-scale operations and customer-experience leadership with new digital-marketing skills — suited to customer-marketing, marketing-operations or CX-marketing roles.",
  "recommended_roles": [
   "Customer / CX Marketing Executive",
   "Marketing Operations Executive",
   "Digital Marketing Coordinator"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior operations/CX leader; marketing is new, so pitch CX/marketing-ops at senior level.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Koh Teck Leong, Alvin (Xu Delong)",
  "email": "alvink2503@gmail.com",
  "years_experience": "15+",
  "industry_background": "Real estate sales & property consultancy",
  "prior_experience_summary": "15+ years as a Senior Real Estate Salesperson across residential, commercial and investment property, with client relationship management, market analysis and digital property marketing.",
  "skills": [
   "Property Sales & Investment Advisory",
   "Digital Property Marketing",
   "Market Analysis",
   "Client Relationship Management (CRM)",
   "Lead Generation",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines long real-estate sales and digital-property-marketing experience with formal digital-marketing skills — a natural fit for real-estate, property-tech or lead-generation marketing roles.",
  "recommended_roles": [
   "Digital Marketing Executive (Real Estate / PropTech)",
   "Property Marketing & Lead Gen Executive",
   "Campaign Marketing Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Property-sales/marketing background; formal marketing rounds it out — entry-to-mid marketing roles fit.",
  "domain": "Real Estate"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Lina Suharjo",
  "email": "Tanlina65@yahoo.com.sg",
  "years_experience": "9+",
  "industry_background": "Engineering & project management (oil & gas), education",
  "prior_experience_summary": "9+ years in engineering and project management at ExxonMobil (cost/schedule engineering, capital projects), more recently a relief teacher integrating digital learning platforms.",
  "skills": [
   "Project Management",
   "Cost & Schedule Engineering",
   "Cross-functional Team Leadership",
   "Process Optimisation",
   "Digital Learning Platforms",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines engineering/project-management discipline with new digital-marketing skills — suited to marketing-operations, project-based marketing or analytical marketing roles.",
  "recommended_roles": [
   "Marketing Operations / Project Executive",
   "Digital Marketing Executive (Analytical)",
   "Marketing Coordinator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Engineering/PM background; marketing is a fresh pivot, so entry-to-mid marketing roles fit.",
  "domain": "Engineering & Manufacturing"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Norman Wang Ann Quang (Wang Anguan)",
  "email": "annquang@yahoo.com.sg",
  "years_experience": "10+",
  "industry_background": "Accounting, audit & e-commerce entrepreneurship",
  "prior_experience_summary": "ACCA-qualified accountant and audit supervisor who also founded an e-commerce brand business (Tigerboywong), building an omni-channel presence with SEO, copywriting and graphic-design skills.",
  "skills": [
   "Accounting & Audit",
   "E-commerce & Brand Building",
   "SEO & Copywriting",
   "Graphic Design (Canva, Procreate)",
   "Digital Marketing",
   "Xero"
  ],
  "skill_marriage": "Combines accounting/audit discipline with hands-on e-commerce entrepreneurship and self-taught SEO/design — a strong fit for e-commerce marketing, SME digital marketing or content-marketing roles.",
  "recommended_roles": [
   "E-commerce / Digital Marketing Executive",
   "Content / SEO Marketing Executive",
   "SME Marketing Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Finance plus real e-commerce/marketing experience; mid-level e-commerce/digital marketing roles fit.",
  "domain": "Marketing & Creative"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Chia Sze Liak, Joshua (Xie Shilie)",
  "email": "joshua@munich.com",
  "years_experience": "20+",
  "industry_background": "Business operations & ownership (automotive, finance, media)",
  "prior_experience_summary": "20+ years across automotive, finance, media and technology in sales, business development, operations and compliance, including running his own vehicle rental/leasing business for 10+ years.",
  "skills": [
   "Operations Management",
   "Business Development",
   "Fleet Management",
   "Stakeholder Management",
   "Contract Negotiation",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines entrepreneurial business-operations and business-development experience with new digital-marketing skills — suited to SME marketing, marketing-operations or business-development marketing roles.",
  "recommended_roles": [
   "Digital Marketing Executive (SME)",
   "Marketing & Business Development Executive",
   "Marketing Operations Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Entrepreneurial ops/BD leader; marketing is new, so pitch at senior-IC with an ops/BD angle.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Chee Li Lin, Gailanne (Xu Lining)",
  "email": "gailanne75@yahoo.com.sg",
  "years_experience": "17+",
  "industry_background": "Real estate sales & marketing",
  "prior_experience_summary": "17+ years as an Associate Senior Marketing Director at Huttons in Singapore real estate, handling residential/commercial property advisory, client needs assessment and transaction management.",
  "skills": [
   "Property Marketing & Advisory",
   "Client Relationship Management",
   "Negotiation",
   "Market Knowledge",
   "Transaction Management",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines long real-estate marketing/advisory experience with formal digital-marketing skills — a natural fit for real-estate, property-tech or client-marketing roles.",
  "recommended_roles": [
   "Digital Marketing Executive (Real Estate / PropTech)",
   "Property Marketing & Lead Gen Executive",
   "Client / CRM Marketing Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior property marketing-director; formal digital marketing rounds it out — mid-to-senior marketing roles fit.",
  "domain": "Real Estate"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Justin Lim Hock Boon (Lin Xuewen Justin)",
  "email": "recoze@yahoo.com.sg",
  "years_experience": "15+",
  "industry_background": "Operations management & technical customer support",
  "prior_experience_summary": "Director overseeing cleaning operations across residential/commercial clients, with earlier experience leading a 22-person technical call-centre team for HP across SEA.",
  "skills": [
   "Operations Management",
   "Team Leadership",
   "Client Servicing",
   "Business Development",
   "Technical Support",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines operations-management and customer-support-leadership experience with new digital-marketing skills — suited to SME marketing, marketing-operations or customer-marketing roles.",
  "recommended_roles": [
   "Digital Marketing Executive (SME)",
   "Marketing Operations Executive",
   "Customer / Service Marketing Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Ops/support-leadership background; marketing is new, so entry-to-mid marketing roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Steve Lam Wai Ming (Lin Weiming)",
  "email": "stevecommand77@gmail.com",
  "years_experience": "20+",
  "industry_background": "Graphic design, video & visual solutions (creative)",
  "prior_experience_summary": "20+ years in graphic design and video editing, most recently Visual Solution Developer at Seatrium, producing motion graphics, marketing content, UI/UX prototypes and 3D visuals.",
  "skills": [
   "Graphic Design & Imaging",
   "Video Editing (Premiere, After Effects)",
   "Motion Graphics / VFX",
   "UI/UX Prototyping",
   "3D Modelling",
   "Digital Marketing (foundational)",
   "Content Creation"
  ],
  "skill_marriage": "Combines deep design/video and visual-solution experience with new digital-marketing skills — can both create rich creative content and run campaigns, ideal for content/creative marketing roles.",
  "recommended_roles": [
   "Content / Creative Marketing Executive",
   "Social Media & Multimedia Marketing Executive",
   "Digital Marketing Designer"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Very experienced creative; marketing is new, so mid-level content/creative marketing roles fit well.",
  "domain": "Marketing & Creative"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Ng Yan Hwa, Joanne (Huang Yanhua)",
  "email": "nyh_joanne@yahoo.com",
  "years_experience": "10+",
  "industry_background": "Broadcast media scheduling & presentation (TV)",
  "prior_experience_summary": "10+ years in broadcast media as scheduler/presentation executive (CNBC, KC Global Media), managing programme schedules, transmission logs, promos and ad placements with scheduling software.",
  "skills": [
   "Broadcast Scheduling",
   "Media Traffic & Ad Placement",
   "Content Coordination",
   "Accuracy & Compliance",
   "Scheduling Software (Landmark, Stratus)",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines broadcast-media scheduling and ad-placement experience with new digital-marketing skills — suited to media-planning, campaign-operations or ad-operations marketing roles.",
  "recommended_roles": [
   "Media / Campaign Operations Executive",
   "Ad Operations / Traffic Executive",
   "Digital Marketing Coordinator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Media-scheduling background; marketing is new, so entry-to-mid media/campaign-ops roles fit.",
  "domain": "Marketing & Creative"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Amos Pang Jia Siong (Feng Jiaxiong)",
  "email": "amospang25@yahoo.com.sg",
  "years_experience": "15+",
  "industry_background": "Industrial/engineering sales & business development",
  "prior_experience_summary": "15+ years in engineering and industrial sales across electronics, automation and semiconductor sectors, with client engagement and market development, currently a private-hire driver exploring digital tools.",
  "skills": [
   "Industrial / B2B Sales",
   "Business Development",
   "Client Relationship Management",
   "Market Research",
   "CRM & Sales Reporting",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines industrial B2B sales and business-development experience with new digital-marketing skills — suited to B2B/industrial marketing, product-marketing or sales-support marketing roles.",
  "recommended_roles": [
   "B2B / Industrial Marketing Executive",
   "Product / Sales Marketing Executive",
   "Digital Marketing Executive (Technical)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Industrial-sales background; marketing is a fresh pivot, so entry-to-mid B2B marketing roles fit.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Callie Tan Hui Feng",
  "email": "callietanhf@yahoo.com.sg",
  "years_experience": "24+",
  "industry_background": "Sales, business development & financial advisory",
  "prior_experience_summary": "24+ years in sales, business development and strategy, starting in financial advisory at AIA, with solution-based selling, roadshows and client relationship management.",
  "skills": [
   "Sales & Business Development",
   "Solution-Based Selling",
   "Client Relationship Management",
   "Market Share Growth",
   "Sales & Marketing Activities",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines long sales/business-development experience with new digital-marketing skills — suited to business-development marketing, B2B marketing or sales-support marketing roles.",
  "recommended_roles": [
   "Business Development & Marketing Executive",
   "B2B / Account-Based Marketing Executive",
   "Digital Marketing Executive"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Very experienced in sales/BD; marketing is new, so pitch business-development marketing at senior-IC.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDM",
  "course_name": "Professional Diploma in Digital Marketing",
  "cohort": "DM-0726",
  "full_name": "Tan Poh Suan (Chen Baoshuang)",
  "email": "baobao_06@yahoo.com.sg",
  "years_experience": "20+",
  "industry_background": "Education & training (curriculum, MOE)",
  "prior_experience_summary": "20+ years in education (MOE) in curriculum planning, training delivery, stakeholder engagement and performance assessment, using digital tools to create learning content.",
  "skills": [
   "Curriculum & Training Delivery",
   "Stakeholder Engagement",
   "Presentation Development",
   "Data Tracking & Reporting",
   "Digital Content Development",
   "Digital Marketing (foundational)"
  ],
  "skill_marriage": "Combines education/training and content-development experience with new digital-marketing skills — suited to content marketing, digital-learning marketing or communications roles.",
  "recommended_roles": [
   "Content Marketing / Communications Executive",
   "Digital Marketing Executive (Education / EdTech)",
   "Marketing Coordinator"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Education/training background; marketing is a fresh pivot, so entry-to-mid content/marketing roles fit.",
  "domain": "Education & Training"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Krishanth Ram Arvin",
  "email": "chrsarvin@gmail.com",
  "years_experience": "15+",
  "industry_background": "Supply chain & logistics operations",
  "prior_experience_summary": "15+ years in supply chain, warehousing, inventory and logistics across APAC, leading process-optimisation and warehouse-transformation projects with Lean Green Belt, KPI reporting and demand planning.",
  "skills": [
   "Supply Chain Management",
   "Warehouse & Inventory Operations",
   "Demand Planning & Forecasting",
   "KPI Reporting & Analysis",
   "Lean / Process Improvement",
   "Data Analysis (foundational)"
  ],
  "skill_marriage": "Combines long supply-chain/logistics operations and KPI-analysis experience with new data-science skills — suited to supply-chain-analytics, logistics-data or operations-analyst roles.",
  "recommended_roles": [
   "Supply Chain / Logistics Data Analyst",
   "Operations / Business Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior supply-chain professional; data science is new, so pitch supply-chain-analytics at senior-IC.",
  "domain": "Supply Chain & Procurement"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Nur Rasyidah Binte Muhamad Ismail Marican",
  "email": "yusyidah2904@gmail.com",
  "years_experience": "8+",
  "industry_background": "Payroll & HR operations",
  "prior_experience_summary": "Senior Payroll Executive managing end-to-end payroll, statutory compliance and reconciliation, preparing and analysing large payroll datasets in Excel with SAP/HRP systems.",
  "skills": [
   "Payroll Processing",
   "Payroll Data Analysis (Excel)",
   "Statutory Compliance",
   "Reconciliation",
   "SAP / HRP Systems",
   "Data Analysis (foundational)"
  ],
  "skill_marriage": "Combines payroll/HR-operations and payroll-data-analysis experience with new data-science skills — suited to HR/payroll analytics, data-quality or reporting-analyst roles.",
  "recommended_roles": [
   "HR / Payroll Data Analyst",
   "Reporting / Data Quality Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Payroll-data background; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "HR & Talent"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Safiyuddin Bin Mohd Nurdin",
  "email": "sbmn97@yahoo.com",
  "years_experience": "40+",
  "industry_background": "Technical, supervisory & training (power electronics, security)",
  "prior_experience_summary": "40+ years of diverse technical, supervisory and training experience across power electronics, information security/forensics and accounting, now pivoting to data engineering and AI development.",
  "skills": [
   "Technical Report Writing & Documentation",
   "Fault / Data Analysis",
   "Power Electronics",
   "Information Security & Forensics",
   "Curriculum / Training",
   "Data Engineering (learning)",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines decades of technical, documentation and training experience with new data-science skills — suited to data-documentation, technical-data-analyst or data-engineering-support roles.",
  "recommended_roles": [
   "Data / Technical Analyst",
   "Junior Data Engineer",
   "Data Documentation / Analysis Analyst"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Very experienced technically but data science is a fresh pivot; entry-to-mid data roles fit despite long tenure.",
  "domain": "Engineering & Manufacturing"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Evanne Sze Toh Min Shi",
  "email": "Evanne.st@gmail.com",
  "years_experience": "15+",
  "industry_background": "Human resources & business partnering (healthcare, MNC)",
  "prior_experience_summary": "15+ years in HR business partnering, expatriate management and workforce planning across healthcare and MNCs, now transitioning into CX and data analytics with Power BI/Excel and AI workflow automation.",
  "skills": [
   "HR Business Partnering",
   "Workforce Planning",
   "Stakeholder Engagement",
   "Data Analytics (Power BI, Excel)",
   "AI Workflow Automation",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines HR-business-partnering and workforce-planning experience with new data-science skills — a strong fit for people-analytics, HR-data or CX-analytics roles.",
  "recommended_roles": [
   "People / HR Analytics Analyst",
   "HR Data / CX Analyst",
   "Business Analyst (HR)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior HR professional; as a data pivot, people-analytics is the natural bridge at senior-IC.",
  "domain": "HR & Talent"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Ivan Yeo Kairong (Yang Kairong, Ivan)",
  "email": "chaoticmagi@gmail.com",
  "years_experience": "10+",
  "industry_background": "Customer service & investigations (e-commerce)",
  "prior_experience_summary": "10+ years in customer service, most recently as an Account Health/Investigation Specialist at Amazon, conducting investigations, appeals and seller guidance, with analytical and problem-solving strengths.",
  "skills": [
   "Customer Service",
   "Investigation & Analysis",
   "Appeals & Case Resolution",
   "Analytical Thinking",
   "Attention to Detail",
   "Data Analysis (foundational)"
  ],
  "skill_marriage": "Combines customer-service and investigation/analysis experience with new data-science skills — suited to operations-analytics, quality-data or junior data-analyst roles.",
  "recommended_roles": [
   "Operations / Quality Data Analyst",
   "Investigation / Insights Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Service/investigation background; data science is new, so entry-level analyst roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Tong Shu Hua",
  "email": "shuhua.tsh@gmail.com",
  "years_experience": "10+",
  "industry_background": "Accounting & finance (full-set, reporting)",
  "prior_experience_summary": "10+ years in accounting/finance across full-set accounts, financial and management reporting, tax, payroll and audit support, with QuickBooks, Xero, AutoCount and SAP.",
  "skills": [
   "Full-Set Accounting",
   "Financial & Management Reporting",
   "Tax & Payroll Compliance",
   "Audit Support",
   "ERP (Xero, SAP, AutoCount)",
   "Data Analysis (foundational)"
  ],
  "skill_marriage": "Combines full-set accounting and financial-reporting experience with new data-science skills — suited to finance-analytics or reporting-analyst roles where accounting-data fluency strengthens analysis.",
  "recommended_roles": [
   "Finance Data Analyst",
   "Reporting / Reconciliation Analyst",
   "Junior Data Analyst (Finance)"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Solid finance background; data science is new, so entry-to-mid finance-analytics roles fit.",
  "domain": "Finance & Accounting"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Lina Tan Lay Nah",
  "email": "linat1309@hotmail.com",
  "years_experience": "20+",
  "industry_background": "Accounting & finance (group consolidation, SGX)",
  "prior_experience_summary": "Finance Manager handling group consolidation across eight entities, financial analysis, budgeting/forecasting and SGX reporting, with SAP FICO implementation and process-improvement project experience.",
  "skills": [
   "Financial Consolidation & Analysis",
   "Budgeting & Forecasting",
   "SAP FICO",
   "Process Improvement",
   "Internal Control",
   "Data Analysis (foundational)"
  ],
  "skill_marriage": "Combines senior finance/consolidation and systems-implementation experience with new data-science skills — suited to finance-analytics, reporting or business-analyst roles grounded in real financial data.",
  "recommended_roles": [
   "Finance Data / Reporting Analyst",
   "Business Analyst (Finance)",
   "BI Analyst (Finance)"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior finance manager; as a data pivot, pitch finance-analytics at senior-IC.",
  "domain": "Finance & Accounting"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Lim Hwei Ching, Christina (Lin Huiqing)",
  "email": "limchristina77@gmail.com",
  "years_experience": "19+",
  "industry_background": "Procurement & supply chain (healthcare, life sciences)",
  "prior_experience_summary": "19 years in procurement and supply chain across healthcare and life sciences, in strategic sourcing, tender management, contract administration and supplier management with SAP/Ariba.",
  "skills": [
   "Strategic Sourcing & Procurement",
   "Tender Management (RFP/RFQ)",
   "Contract & Supplier Management",
   "Category Management",
   "SAP & Ariba",
   "Data Analysis (foundational)"
  ],
  "skill_marriage": "Combines long procurement/supply-chain experience with new data-science skills — suited to procurement-analytics, supply-chain-data or spend-analyst roles.",
  "recommended_roles": [
   "Procurement / Supply Chain Data Analyst",
   "Spend / Category Analyst",
   "Business Analyst (Procurement)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior procurement professional; data science is new, so pitch procurement-analytics at senior-IC.",
  "domain": "Supply Chain & Procurement"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Lin Rongfeng, Dave (Lin Rongfeng)",
  "email": "daverflin@gmail.com",
  "years_experience": "18+",
  "industry_background": "Internal audit, risk & governance (Big Four, MNC)",
  "prior_experience_summary": "18+ years leading internal audit, internal control and enterprise risk management across Big Four and MNCs (Burberry, LVMH, Cathay Pacific), an early adopter of data analytics in audit across up to 40 entities.",
  "skills": [
   "Internal Audit & Controls",
   "Enterprise Risk Management",
   "Governance & Compliance",
   "Data Analytics in Audit",
   "AI / Automation in GRC",
   "Data Analysis (foundational)"
  ],
  "skill_marriage": "Combines senior audit/risk/governance leadership and early data-analytics-in-audit experience with new data-science skills — a strong fit for audit-analytics, risk-data or GRC-analytics roles.",
  "recommended_roles": [
   "Audit / Risk Data Analyst",
   "GRC Analytics Analyst",
   "Business Analyst (Risk / Controls)"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior audit/risk leader with data-analytics exposure; genuinely ready for audit/risk-analytics at senior level.",
  "domain": "Finance & Accounting"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Manpreet Kaur",
  "email": "mannukaur2901@gmail.com",
  "years_experience": "9+",
  "industry_background": "Operations & administration (corporate, education)",
  "prior_experience_summary": "~9 years in corporate operations and administration (Shooklin & Bok), managing office operations, procurement, cost tracking (Excel), vendor coordination and business support across corporate and education sectors.",
  "skills": [
   "Operations & Admin Management",
   "Procurement & Vendor Coordination",
   "Cost Tracking & Reporting (Excel)",
   "Client Servicing",
   "Process Coordination",
   "Data Analysis (foundational)"
  ],
  "skill_marriage": "Combines operations/administration and cost-tracking experience with new data-science skills — suited to operations-analytics, reporting or junior data-analyst roles.",
  "recommended_roles": [
   "Operations / Business Data Analyst",
   "Reporting Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Ops/admin background; data science is new, so entry-to-mid analyst roles fit.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Pong Miew Chin, Kelly",
  "email": "miewchin@gmail.com",
  "years_experience": "20+",
  "industry_background": "Supply chain, logistics & commercial support",
  "prior_experience_summary": "20 years in supply chain, logistics operations and commercial support, covering demand planning, purchasing, order processing, inventory, import/export and ERP master-data across APAC/EU/US markets.",
  "skills": [
   "Supply Chain & Logistics Operations",
   "Demand Planning",
   "Inventory Management",
   "Import / Export & Trade Documentation",
   "ERP & Master Data",
   "Data Analysis (foundational)"
  ],
  "skill_marriage": "Combines long supply-chain/logistics and commercial-support experience with new data-science skills — suited to supply-chain-analytics, logistics-data or operations-analyst roles.",
  "recommended_roles": [
   "Supply Chain / Logistics Data Analyst",
   "Operations / Demand Analyst",
   "Junior Data Analyst"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior supply-chain professional; data science is new, so pitch supply-chain-analytics at senior-IC.",
  "domain": "Supply Chain & Procurement"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDS",
  "course_name": "Professional Diploma in Data Science",
  "cohort": "DS-0726",
  "full_name": "Flora Tan Meng Eng",
  "email": "flora_tme@hotmail.com",
  "years_experience": "30+",
  "industry_background": "Digital transformation & IT programme management (banking, aviation)",
  "prior_experience_summary": "30+ years leading large-scale IT and business transformation programmes across banking and aviation (Singapore Airlines), managing $2M-$10M portfolios, Agile delivery and data-driven transformation.",
  "skills": [
   "Digital Transformation",
   "IT Portfolio & Programme Management",
   "Agile Delivery",
   "Data-Driven Decision Making",
   "Stakeholder Management",
   "Change Management",
   "Data Science (foundational)"
  ],
  "skill_marriage": "Combines senior IT/business-transformation leadership with new data-science skills — suited to data/analytics programme management, data-product or transformation-analytics leadership roles.",
  "recommended_roles": [
   "Data / Analytics Programme Manager",
   "Digital Transformation (Data) Lead",
   "Business Analyst (Data Platforms)"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Very senior transformation leader; best positioned leading data/analytics delivery rather than hands-on data-scientist roles.",
  "domain": "Project Management"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Jace Hung Chia Fen",
  "email": "jacehung@gmail.com",
  "years_experience": "10+",
  "industry_background": "Sales & business development (cybersecurity, tech)",
  "prior_experience_summary": "Sales Manager at a cybersecurity firm driving end-to-end sales, pipeline building and consultative selling, with stakeholder engagement, programme coordination and partnership development.",
  "skills": [
   "Sales & Business Development",
   "Consultative Selling",
   "Stakeholder Engagement",
   "Partnership Development",
   "Customer Relationship Management",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines sales/business-development and partnership experience with new digital-innovation skills — suited to digital-solutions sales, business-analyst or transformation-support roles in tech.",
  "recommended_roles": [
   "Digital Solutions / Business Development Executive",
   "Business Analyst (Tech / Digital)",
   "Digital Transformation Support Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Sales/BD background; digital-innovation is new, so mid-level digital-BD/BA roles fit.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Cheryl Ng Shu Hui (Huang Shuhui)",
  "email": "cheryl191080@gmail.com",
  "years_experience": "10+",
  "industry_background": "Sports industry events, marketing & customer service",
  "prior_experience_summary": "Sales/marketing-communications executive with sports-industry experience (SG Basketball Academy) in event coordination, customer service and operations, building digital-marketing and content skills.",
  "skills": [
   "Event Coordination",
   "Marketing Communications",
   "Customer Service",
   "Content Creation (learning)",
   "Stakeholder Management",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines event-coordination and marketing-communications experience with new digital-innovation skills — suited to digital-marketing-support, event-tech or community-engagement roles.",
  "recommended_roles": [
   "Digital Marketing / Communications Executive",
   "Event / Community Engagement Executive",
   "Business Support / Coordination Executive"
  ],
  "seniority": "Individual Contributor",
  "seniority_note": "Events/marketing-comms background; digital skills are newly building, so entry-to-mid roles fit.",
  "domain": "Marketing & Creative"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Quek Shian Pin (Guo Xianbin)",
  "email": "shian_pin@hotmail.com",
  "years_experience": "15+",
  "industry_background": "Operations & general management (EV automotive, engineering)",
  "prior_experience_summary": "General Manager of an EV dealership (BYD) overseeing sales, after-sales and operations, using AI tools and CRM automation, with a power-engineering MSc and cross-sector operations/PM background.",
  "skills": [
   "Operations & General Management",
   "Project Management",
   "CRM & Automation (PepperCloud)",
   "AI Tools for Analysis",
   "Stakeholder Management",
   "Digital Innovation Tools",
   "Power Engineering"
  ],
  "skill_marriage": "Combines operations/general-management and hands-on AI/CRM-automation experience with new digital-innovation skills — suited to operations-digitalisation, business-transformation or business-analyst roles.",
  "recommended_roles": [
   "Operations / Business Transformation Analyst",
   "Digital Innovation / Automation Executive",
   "Business Analyst (Operations)"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior GM with real AI/automation adoption; digital-innovation complements strongly — pitch transformation/BA at senior level.",
  "domain": "Operations & Admin"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Seah Hou Liang",
  "email": "micseahh@gmail.com",
  "years_experience": "25+",
  "industry_background": "IT project management & administration (education, computing)",
  "prior_experience_summary": "Administrative/IT manager with 19 years in computing and 11 in education, leading ERP/IT infrastructure implementation, acting as project manager and functional architect across the IT project lifecycle.",
  "skills": [
   "IT Project Management",
   "ERP Implementation",
   "Functional Architecture",
   "Team & Vendor Leadership",
   "Workflow Optimisation",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines IT-project-management and ERP-implementation experience with new digital-innovation skills — a strong fit for digital-project-management, business-analyst or transformation-delivery roles.",
  "recommended_roles": [
   "Digital Project Manager",
   "Business Analyst (IT / ERP)",
   "Digital Transformation Delivery Analyst"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior IT-PM/architect; genuinely ready for digital-PM or transformation-delivery roles.",
  "domain": "IT & Infrastructure"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Chan Siew Yin, Amy",
  "email": "chansy.amy@gmail.com",
  "years_experience": "30+",
  "industry_background": "Banking, financial services & administration",
  "prior_experience_summary": "30+ years across banking, financial services, education and administration, with financial analysis, risk, operations/process improvement, client relationship management and MAS/IBF compliance.",
  "skills": [
   "Financial Analysis & Risk",
   "Operations & Process Improvement",
   "Client Relationship Management",
   "Data Analysis & Reporting",
   "Regulatory Compliance (MAS/IBF)",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines long banking/financial-services and process-improvement experience with new digital-innovation skills — suited to finance-digitalisation, operations-transformation or business-analyst roles in financial services.",
  "recommended_roles": [
   "Business Analyst (Financial Services)",
   "Operations / Process Transformation Analyst",
   "Digital Innovation Executive (Finance)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Very experienced in banking/ops; digital-innovation is new, so pitch finance-transformation/BA at senior-IC.",
  "domain": "Banking & Wealth"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Tham Chee Chong, Travis (Tan Zhizhong)",
  "email": "TRAVIS.THAM@GMAIL.COM",
  "years_experience": "15+",
  "industry_background": "Technical/industrial sales & business development (lighting, semiconductor)",
  "prior_experience_summary": "Sales Manager at Ushio Asia Pacific leading high-pressure-lamp and LED sales across SE Asia, developing new business (Grow Light projects), sales targets/KPIs and production-forecast analysis.",
  "skills": [
   "Technical / Industrial B2B Sales",
   "Business Development",
   "Sales KPI & Forecast Analysis",
   "Partner Development",
   "Negotiation",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines industrial B2B sales and business-development experience with new digital-innovation skills — suited to sales-digitalisation, business-development or transformation-support roles in technical sectors.",
  "recommended_roles": [
   "Business Development / Digital Solutions Executive",
   "Sales Operations / Transformation Analyst",
   "Business Analyst (Technical Sales)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior industrial-sales professional; digital-innovation is new, so pitch digital-BD/transformation at senior-IC.",
  "domain": "Sales & Business Development"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Teo Wee Kin (Zhang Weiquan)",
  "email": "teoweekin@gmail.com",
  "years_experience": "25+",
  "industry_background": "MRO / advanced manufacturing operations (aerospace)",
  "prior_experience_summary": "25+ years in MRO digital-factory operations and advanced aerospace manufacturing, leading global teams (420 staff, US$35M output), supply chain, digital transformation and operational excellence (Lean Six Sigma).",
  "skills": [
   "MRO / Manufacturing Operations",
   "Digital Factory / Transformation",
   "Programme & Supply Chain Management",
   "Lean Six Sigma",
   "Team & P&L Leadership",
   "Digital Innovation Tools",
   "Process Improvement"
  ],
  "skill_marriage": "Combines senior aerospace-manufacturing operations and digital-factory transformation leadership with new digital-innovation skills — strong fit for manufacturing-digitalisation, Industry-4.0 or operations-transformation leadership roles.",
  "recommended_roles": [
   "Manufacturing Digital Transformation Lead",
   "Operations / Process Innovation Manager",
   "Digital Transformation Consultant"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Very senior operations/transformation leader; best positioned in transformation-lead roles leveraging manufacturing depth.",
  "domain": "Engineering & Manufacturing"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Tye Kuo Wei (Dai Guowei)",
  "email": "kuowei.tye@gmail.com",
  "years_experience": "20+",
  "industry_background": "Strategic sourcing & procurement (infrastructure)",
  "prior_experience_summary": "20+ years in regional strategic sourcing and procurement of electrical infrastructure (switchgears, transformers), with category strategy, supplier management, risk governance and procurement analytics (Power BI).",
  "skills": [
   "Strategic Sourcing & Procurement",
   "Category Strategy",
   "Supplier / Risk Management",
   "Procurement Analytics (Power BI)",
   "Power Automate / GenAI (learning)",
   "Digital Innovation Tools"
  ],
  "skill_marriage": "Combines senior procurement/sourcing and procurement-analytics experience with new digital-innovation skills — suited to procurement-digitalisation, supply-chain-analytics or digital-transformation roles in sourcing.",
  "recommended_roles": [
   "Procurement / Supply Chain Digital Transformation Analyst",
   "Spend Analytics / Sourcing Analyst",
   "Business Analyst (Procurement)"
  ],
  "seniority": "Senior IC",
  "seniority_note": "Senior procurement leader building digital/analytics skills; pitch procurement-digitalisation/analytics at senior-IC.",
  "domain": "Supply Chain & Procurement"
 },
 {
  "specialist": "Preetika",
  "course_code": "PDDI",
  "course_name": "Professional Diploma in Digital Innovation",
  "cohort": "DI-0726",
  "full_name": "Helena Woo Xiu Ying",
  "email": "",
  "years_experience": "20+",
  "industry_background": "Banking operations & vendor management (private/consumer banking)",
  "prior_experience_summary": "20+ years in banking operations at DBS and Societe Generale, rising to Assistant Vice President in service-delivery and outsource-operations management, sourcing and vendor management in consumer banking.",
  "skills": [
   "Banking Operations",
   "Vendor & Sourcing Management",
   "Service Delivery Management",
   "Process Improvement",
   "Stakeholder Management",
   "Digital Innovation Tools (foundational)"
  ],
  "skill_marriage": "Combines long banking-operations and vendor-management experience with new digital-innovation skills — suited to banking-operations digitalisation, process-transformation or business-analyst roles in financial services.",
  "recommended_roles": [
   "Business Analyst (Banking Operations)",
   "Operations / Process Transformation Analyst",
   "Digital Innovation Executive (Financial Services)"
  ],
  "seniority": "Senior IC / Managerial upside",
  "seniority_note": "Senior banking-ops (AVP) professional; digital-innovation is new, so pitch operations-transformation/BA at senior level.",
  "domain": "Banking & Wealth"
 }
]
