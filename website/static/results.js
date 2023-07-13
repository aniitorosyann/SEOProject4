
    document.getElementById('search-button').addEventListener('click', function() {
        let searchCategory = document.getElementById('search-category').value;
        let searchTerm = document.getElementById('search-term').value;

        fetch('/api/data?category=' + searchCategory + '&value=' + searchTerm)
            .then(response => response.json())
            .then(data => {
                let filteredData = data.filter(car => car[searchCategory].toLowerCase().includes(searchTerm.toLowerCase()));

                let htmlString = '';
                for (let car of filteredData) {
                    htmlString += `<p>${car[1]} ${car[2]} (${car[3]}) - Type: ${car[4]}</p>`;
                    htmlString += `<p>${car.make} ${car.model} (${car.year}) - Type: ${car.type}</p>`;
                }

                document.getElementById('search-results').innerHTML = htmlString;
            });
    });

