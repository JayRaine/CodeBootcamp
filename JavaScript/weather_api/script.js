const apiKey = '434bf09e7de43630c7aabd31c2440c2e';
const cityElement = document.querySelector('.city-name');
const tempElement = document.querySelector('.temperature');
const descriptionElement = document.querySelector('.weather-description');
const iconElement = document.querySelector('.weather-icon');

const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid=${apiKey}`;

function fetchWeatherData(cityName) {
  const apiUrlWithCity = apiUrl.replace('{CITY_NAME}', cityName);

  fetch(apiUrlWithCity)
    .then((response) => response.json())
    .then((data) => {
      cityElement.textContent = data.name;
      tempElement.textContent = `${(data.main.temp - 273.15).toFixed(1)}°C`;
      descriptionElement.textContent = data.weather[0].description;
      iconElement.setAttribute(
        'src',
        `http://openweathermap.org/img/wn/${data.weather[0].icon}.png`
      );
    })
    .catch((error) => {
      console.error('Error fetching weather data:', error);
      cityElement.textContent = 'City Not Found';
      tempElement.textContent = 'N/A';
      descriptionElement.textContent = '';
      iconElement.setAttribute('src', '');
    });
}

// You can call the fetchWeatherData function with any city name you want
const cityName = 'Manchester'; // Replace 'YOUR_CITY_NAME' with the desired city name
fetchWeatherData(cityName);
