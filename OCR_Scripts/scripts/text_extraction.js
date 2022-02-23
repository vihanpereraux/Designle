// Reading the uploaded image
function imgFunction(event)
{
    // accessing url of the <img> attribute
    var outputUrl = document.getElementById('output').src;
    
    // setting the url
	outputUrl = URL.createObjectURL(event.target.files[0]);

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
        { logger: message => console.log( message ) }
    )
    .then
    (({ data: { text } }) => 
        {
            analyzingData(text);
        }
    )
}



function analyzingData(text)
{
    var extractedText = text;
    document.getElementById("text").innerHTML = extractedText;
    console.log(extractedText);

    // extracted text to an array
    var textArray = extractedText.split(" ");
    console.log(textArray);

    // length of the extracted text
    console.log(textArray.length);

    // element storing array
    let randomNumbers = [];
    let selectedTextArray = [];
    
    for (let i = 0; i < 5; i++) 
    {
        let randomNumber = Math.floor(Math.random() * textArray.length) + 1;
        // preventing number repitition
        while (randomNumbers.includes(randomNumber)) 
        {
            randomNumber = Math.floor(Math.random() * textArray.length) + 1;
        }
        randomNumbers.push(randomNumber);
        
        // saving selected word in selectedTextArray[]
        console.log(textArray[randomNumbers[i]]);       
    }
}
