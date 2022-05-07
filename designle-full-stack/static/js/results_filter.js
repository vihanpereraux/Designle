// Accesssing the filter button
var filterButton = document.getElementById("filterBtn");

// arrays for sorting suggestions
var relevantSuggestions = [];
var otherSuggestions = [];

var filteredResults = document.getElementById('filtered-results');

filterButton.onclick = function(){
    $.ajax({
        url: "/about",
        type: "POST",
        data: {},
        success: function(response) {
            if ( JSON.parse(localStorage.getItem('category')) != null ){
                var userCategory = JSON.parse(localStorage.getItem("category")); // user selected category
                for (let i = 0; i < response.data[0].length; i++) {
                    if (response.data[0][i].category == userCategory){
                        relevantSuggestions.push(response.data[0][i].suggestion);
                    }
                    else{
                        otherSuggestions.push(response.data[0][i].suggestion);
                    }
                }

                for (let j = 0; j < otherSuggestions.length; j++) {
                    relevantSuggestions.push(otherSuggestions[j]);
                }

                for (let k = 0; k < relevantSuggestions.length; k++) {
                    var filteredItem = `<li><p>${relevantSuggestions[k]}</p></li>`
                    filteredResults.innerHTML += filteredItem;
                }
                
                console.log(response.data[0][0].category);
                console.log(relevantSuggestions);
            }
            else{
                alert('First select color usages and get all recommendations !')
            }
        }
    });
}