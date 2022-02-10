var greenArray = [];

fetch('data/something.json')
    .then(response => response.text())
    .then(data => 
    {
  	    // Do something with your data  
        for (let i = 1; i < 21; i++) 
        {
            greenArray.push(JSON.parse(data)[i]);
        }
        setLocalStorage();
    });

function setLocalStorage()
{
    localStorage.setItem("greenArray", JSON.stringify(greenArray));
    console.log("Added to the local stoeage");
} 