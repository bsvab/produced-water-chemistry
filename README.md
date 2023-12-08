# Project 1 Proposal

## <p style="color:#CC6600">Topic:</p> 
Python-Based Analysis and Visualization of Produced Water Chemistry for Environmental and Agricultural Utilization

<ins>Team Members</ins>: <br>
Roxana Darvari, Brittany Svab, John Cahill, Alejandro Juarez, Sarah Cain

## <p style="color:#CC6600">Introduction:</p> 
The proposed project aims to develop a Python-based tool for analyzing and visualizing geochemical data of produced water, the generally salty water that is produced from the subsurface, along with the target resource, primarily oil and gas. The project's objective is to assess the feasibility of treating the produced water to fresh water standard for environmental flow (complement natural stream flow) and irrigation purposes. The methodology involves data cleansing and filtering to eliminate unsuitable samples and manage censored data, followed by a thorough analysis to identify redundant samples. The main objective is to assess concentration of elements causing adverse conditions, such as scaling, during water treatment operations. The project will also explore lithium availability. Lithium has been categorized as a critical element by the US Government. Visualization techniques, including mapping elemental compositions, will be employed to represent the data effectively.

## <p style="color:#CC6600">Objectives:</p> 

### <p style="color:#CC9900">Data Cleansing and Filtering:</p> 
-	Eliminate samples with Total Dissolved Solids (TDS) below seawater concentration (35,000 ppm).
-	Exclude samples lacking either sodium (Na) or chloride (Cl) analyses.
-	Implement tests for elemental ratios (Na>Ca, Cl>SO4, Ca>Mg/2) and remove failing samples, which represent unnatural combinations.
-	Manage censored data effectively.

### <p style="color:#CC9900">Data Analysis:</p> 
-	Identify redundant samples from the same location but different dates, retaining only the most recent.
-	Analyze and list elements causing scaling in water treatment (calcium, magnesium, carbonate, bicarbonate, silica, iron, barium, strontium), and assess lithium (Li) availability.

### <p style="color:#CC9900">Visualization:</p> 
-	Create visualizations to represent the count of missing elements.
-	Determine and map the most common combinations of missing elements.
-	Perform a cluster analysis to investigate geographical correlations within the data.
-	Generate Piper plots to illustrate the chemical characteristics of water samples.
-	Compare elemental compositions based on depth and across different states.
-	Visualize Li availability across the study area.

### <p style="color:#CC9900">Database Utilization:</p> 
-	Employ data from the US Geological Survey (USGS), available at https://www.sciencebase.gov/catalog/item/59d25d63e4b05fe04cc235f9 and the internal Bureau of Economic Geology (BEG) databases.
-	Analyze and compare two versions of the database: one with numerical values (USGSPWDBv2.3n.xlsx) and another including censored data (USGSPWDBv2.3c.xlsx).

### <p style="color:#CC9900">Purpose of Produced Water Treatment:</p> 
- The primary goal is to assess the potential of treated produced water for irrigation and environmental flow, emphasizing sustainable water management practices.

### <p style="color:#CC9900">Methodology:</p> 
-	Utilize Python for data processing, analysis, and visualization.
-	Employ libraries such as Pandas for data manipulation, Matplotlib and Seaborn for visualization, and Scikit-learn for clustering analysis.

### <p style="color:#CC9900">Expected Outcomes:</p> 
-	A comprehensive understanding of the geochemical profile of produced waters.
-	Identification of potential challenges and opportunities in using produced water for environmental and agricultural purposes.
-	A set of interactive, informative visualizations aiding in the interpretation of the geochemical data.

### <p style="color:#CC9900">Relevance and Impact:</p> 
- This project aligns with current environmental and water resource management needs, offering a practical approach to repurposing produced water, thereby contributing to more sustainable practices in the industry
