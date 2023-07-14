document.getElementById('search-button').addEventListener('click', async function() {
    let searchCategory = document.getElementById('search-category').value;
    let searchTerm = document.getElementById('search-term').value;
    const url = `https://car-data.p.rapidapi.com/cars?limit=10&page=0&${searchCategory}=${searchTerm}`;
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '2a797d883emshc91e96215000877p1c9e9ajsn434f39ac6d62',
            'X-RapidAPI-Host': 'car-data.p.rapidapi.com'
        }
    };
    try {
        const response = await fetch(url, options);
        const data = await response.json();
        let htmlString = '';
        if (data.length === 0) {
            htmlString = '<p>No Results</p>';
        } else {
            for (let car of data) {
                htmlString += `<p>${car.make} ${car.model} (${car.year}) - Type: ${car.type}</p>`;
            }
        }
        document.getElementById('search-results').innerHTML = htmlString;
    } catch (error) {
        console.error(error);
    }
});