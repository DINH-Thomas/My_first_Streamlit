## Challenge - Plotly CO2 Emissions 🌎

![](https://images.unsplash.com/photo-1581094794329-c8112a89af12?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)

Photo by [Methane Emissions](https://unsplash.com/@methane)

## Objectives

Today you will work with CO2 emissions data from countries worldwide and learn how to create interactive visualizations using Plotly.

The dataset contains **CO2 per capita** emissions for multiple countries across different years, allowing you to explore global emission trends and patterns.

The goal of this challenge is to:

- Load and explore CO2 emissions data
- Create interactive geographic visualizations using Plotly Express
- Build scatter geo maps and choropleth maps
- Add animations to visualize changes over time
- Enhance visualizations with geographic data (continents)
- Create custom functions for data visualization

## Guidelines

You are free to explore the data the way you want. However, we recommend following the notebook structure provided in `src/Plotly-CO2-emissions.ipynb`.

**1. Data Loading**

1. Load the `CO2_per_capita.csv` dataset into a Pandas DataFrame
2. Explore the data structure using `.info()`, `.describe()`, and `.head()`
3. Understand what information is contained in the dataset

**2. Geographic Visualizations**

1. Create scatter geo maps to visualize CO2 emissions by country
2. Add year-based animations to see emissions change over time
3. Enhance maps with continent information for color coding
4. Build choropleth maps for different visualization styles
5. Create bar charts showing top emitters with continent-based coloring

**3. Advanced Features**

1. Build reusable functions for creating visualizations
2. Implement filtering by year ranges and top N countries
3. Customize colors, sizes, and hover information
4. Experiment with different map projections and color scales

**🔎 Hints**

- Start by understanding the data structure before creating visualizations
- Use Plotly Express (`px`) for quick and interactive visualizations
- Remember to merge geographic data (continents) with your CO2 data
- Try different color scales and projections to make your visualizations more appealing
- Test your functions with different parameters to ensure they work correctly

### 💻 **Local work (on your computer)**

Open `src/Plotly-CO2-emissions.ipynb` with Jupyter notebook.

Local work requires a complete setup first. Please check this menu item **[`🔧`](https://lxp.artefact.com/python-setup)** and follow the guidelines corresponding to your operating system (OS).

