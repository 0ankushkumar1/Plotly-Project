# India Census Data Analysis

This is a Streamlit-based application designed for analyzing and visualizing census data of India at various levels, including district, state, and the entire country. The application provides interactive visualizations, such as scatter maps, pie charts, bar charts, and histograms, to explore demographic, social, and economic data.

## Features

- **Dynamic Level of Analysis**: Choose between district, state, or national-level analysis.
- **Interactive Visualizations**: Explore data through scatter maps, pie charts, bar charts, and histograms.
- **Customizable Parameters**: Select data attributes to generate custom plots.
- **Clean and Modular Code**: Reusable functions for data processing and visualization.

## Installation

### Prerequisites
- Python 3.7 or higher
- Required Python libraries:
  - `numpy`
  - `pandas`
  - `plotly`
  - `streamlit`

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd india-census-analysis
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Place the required datasets in the project directory:
   - `india-districts-census-2011.csv`
   - `district wise centroids.csv`

5. Run the application:
   ```bash
   streamlit run optimized_census_app.py
   ```

## Usage

1. **Launch the Application**: Open the application in your browser using the link provided by Streamlit.
2. **Choose Level of Analysis**:
   - `District`: View data and visualizations for a specific district.
   - `State`: Analyze aggregated data for a selected state.
   - `India`: Explore nationwide trends and distributions.
3. **Interact with Visualizations**: Use the sidebar to select specific parameters or toggle between visualizations.

## Data Sources
- **Demographic Data**: Based on the 2011 Census of India.
- **Geographic Coordinates**: District centroids for mapping.

## File Structure
- `optimized_census_app.py`: Main application script.
- `india-districts-census-2011.csv`: Census data.
- `district wise centroids.csv`: Geographic coordinates for districts.
- `requirements.txt`: List of required Python libraries.

## Visualizations
- **Scatter Map**: View population and sex ratio distribution geographically.
- **Pie Chart**: Analyze social and caste-based distributions.
- **Bar Chart**: Explore workforce, education, or household data.
- **Histogram**: Visualize age group distributions.

## Customization
The modular structure allows easy customization and extension:
- **Add New Visualizations**: Use the `create_plot` function to introduce new types of charts.
- **Modify Data Processing**: Update the `load_and_preprocess_data` function to incorporate additional transformations.

## Contributing
Contributions are welcome! If you find a bug or have suggestions for improvement, please open an issue or submit a pull request.



