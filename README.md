# CineCompass

🍿 CineCompass is a simple movie recommendation system that suggests movies based on user preferences using machine learning techniques.

## Table of Contents

- [CineCompass](#cinecompass)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Requirements](#requirements)
  - [Usage](#usage)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [How It Works](#how-it-works)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   ### Requirements

   The following Python packages are required for this project:

   ```
   pandas==1.5.3
   numpy==1.23.5
   nltk==3.7
   scikit-learn==1.0.2
   ```

3. Ensure you have an API key for [The Movie Database (TMDb)](https://www.themoviedb.org/) to fetch movie posters.

## Usage

1. Start the Streamlit application:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application.

3. Select your favorite movie from the dropdown list, and click the "Recommend" button to get movie recommendations.

## Features

- Fetches movie data and posters from The Movie Database (TMDb).
- Provides recommendations based on user-selected movies.
- Beautifully designed user interface with customized styles.

## Technologies Used

- Python
- Streamlit
- Pandas
- Requests
- Pickle (for loading pre-trained models and datasets)
- The Movie Database (TMDb) API

## How It Works

1. **Data Preparation**: Movie data is loaded from a pickle file into a Pandas DataFrame.
2. **Similarity Calculation**: A precomputed similarity matrix is used to find similar movies.
3. **User Interaction**: Users select a movie from the dropdown, and the app fetches recommendations based on the chosen movie.
4. **Displaying Results**: Recommended movies and their posters are displayed on the web application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any features or improvements you'd like to suggest.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
