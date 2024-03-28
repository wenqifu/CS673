function getWeather() {
    const location = document.getElementById("location-input").value;
    const apiKey = "abb1780de66e8ba08a5a0207b0a58b65"; // Replace with your OpenWeatherMap API Key
    const url = `http://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=metric`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            const { main, weather } = data;
            const displayDiv = document.getElementById("weather-display");
            displayDiv.innerHTML = `
                <h2>Weather in ${location}</h2>
                <p>Temperature: ${main.temp}°C</p>
                <p>Feels Like: ${main.feels_like}°C</p>
                <p>Description: ${weather[0].description}</p>
            `;
        })
        .catch(error => {
            console.error("Error fetching weather data:", error);
        });
}
