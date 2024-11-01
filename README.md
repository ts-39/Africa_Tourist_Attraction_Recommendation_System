# Africa Tourist Attraction Recommendation System

This repository hosts a recommendation system designed to highlight and recommend tourist attractions across Africa. The system was inspired by my experience as the leader of an international cooperation club during high school, where I became aware of Africa's economic challenges and recognized its vast cultural and touristic potential. This project aims to encourage travel to African destinations by providing insightful recommendations based on cultural and gastronomic features.

## Project Overview

The Africa Tourist Attraction Recommendation System uses data from Wikipedia entries of African cities to assess their appeal in various tourist-friendly categories. Key data points include mentions of terms related to food, culture, history, and natural beauty, which are used to generate a recommendation score for each city.

## Features

- **Data Collection**: Data for each city is collected from Wikipedia, focusing on the frequency of certain keywords in each entry. For instance, words associated with cuisine such as "food," "cuisine," "restaurant," and "local dishes" are counted to create a feature representing the city’s food appeal.
  
- **Recommendation Model**: The model leverages a nearest neighbors algorithm, implemented using `from sklearn.neighbors import NearestNeighbors`, to suggest cities with similar features to the user’s preferences.

- **Web Application**: The app is accessible online, allowing users to interact with the recommendation system directly. You can explore the recommendations at this [link](https://africatouristattractionrecommendationsystem-cgpzq2xhhfj7jdbwk6.streamlit.app/).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ts-39/Africa_Tourist_Attraction_Recommendation_System.git
   cd Africa_Tourist_Attraction_Recommendation_System
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Processing**: The system reads Wikipedia data for each city, processing keyword counts in categories like food, history, and culture.
  
2. **Model Training**: Using the processed data, the model is trained to recognize similarities among cities, allowing it to make personalized recommendations based on user input.

3. **Making Recommendations**:
   - Run the main script to receive suggestions based on the specified preferences.
   ```bash
   python recommend.py
   ```

## Example

Here’s how you can run the recommendation system with example inputs:

```bash
python recommend.py --preferences "food, history"
```

The system will return a list of cities that match the input preferences based on the model's similarity assessment.

## Future Improvements

- **Enhanced Data Collection**: Expanding the data collection to include more detailed features such as historical landmarks and festivals.
- **Refined Model**: Exploring alternative recommendation algorithms for improved accuracy and diversity in recommendations.

---

This README should give potential users and contributors a comprehensive understanding of the project and how to use it. Let me know if you’d like further customization!
