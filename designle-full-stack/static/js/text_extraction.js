// Reading the uploaded image
function imgFunction(event)
{
    // accessing url of the <img> attribute
    // var outputUrl = document.getElementById('output').src;
    document.getElementById("myBtn").disabled = true;
    
    // setting the url
	var outputUrl = URL.createObjectURL(event.target.files[0]);

    // calling the OCR function
    extractText(outputUrl);
}


// OCR process starts from here
function extractText(imageUrl)
{    
    Tesseract.recognize
    ( 
        imageUrl,
        'eng',
        { logger: extractionStatus => console.log( extractionStatus ) }
    )
    .then
    (({ data: { text } }) => 
        {
            processData(text);
        }
    )
}


// Pre processing extracted data
// an array to store cleaned data
var cleanedText = [];

function processData(extractedText)
{   
    console.log(extractedText); // for checking purpsoe

    // extracted text to an array
    var textArray = extractedText.split(" ");
    console.log(textArray); // for checking purpsoe
    
    // regex to clean the data
    var specialCharacters = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;

    // regex to filter line breakers
    var lineBreakers = /(\r\n|\n|\r)/gm;

    // filling cleanedText[] with filtered data
    for (let i = 0; i < textArray.length; i++) 
    {
        if (!specialCharacters.test(textArray[i])) 
        {
            cleanedText.push(textArray[i].replace(lineBreakers, " "));
        }
    }

    console.log(cleanedText);
    // saving cleaned data in local storage
    localStorage.setItem("cleanedText", JSON.stringify(cleanedText));

    if (cleanedText != null){
        document.getElementById("myBtn").disabled = false;
    }
}

