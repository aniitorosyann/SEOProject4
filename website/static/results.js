//add event listener
    document.getElementById('search-button').addEventListener('click', function() {
        //GET INFO:  category & term
        let searchCategory = document.getElementById('search-category').value;
        let searchTerm = document.getElementById('search-term').value;

        fetch('/api/data?category=' + searchCategory + '&value=' + searchTerm)
            .then(response => response.json())
            .then(data => {
                let htmlString = '';
                
                //loop through each item in the array
                if (data.length == 0){
                     htmlString = '<p>No Results</p>';
                }
                else{
                    //let filteredData = data.filter(car => car[searchCategory].toLowerCase().includes(searchTerm.toLowerCase()));

                    //append a string to for each car to give the user info
                    for (let car of data) {
                        htmlString += `<p>${car[1]} ${car[2]} (${car[3]}) - Type: ${car[4]}</p>`;
                        //htmlString += `<p>${car.make} ${car.model} (${car.year}) - Type: ${car.type}</p>`;
                    }
                }
                // assing search results to display later
                document.getElementById('search-results').innerHTML = htmlString;
            });
    });

