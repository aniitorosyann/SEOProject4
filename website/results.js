
    document.getElementById('search-button').addEventListener('click', function() {
        let searchCategory = document.getElementById('search-category').value;
        let searchTerm = document.getElementById('search-term').value;

        fetch('/api/data')
            .then(response => response.json())
            .then(data => {
                let filteredData = data.filter(car => car[searchCategory].toLowerCase().includes(searchTerm.toLowerCase()));

                let htmlString = '';
                for (let car of filteredData) {
                    htmlString += `<p>${car.make} ${car.model} (${car.year}) - Type: ${car.type}</p>`;
                }

                document.getElementById('search-results').innerHTML = htmlString;
            });
    });

