extractText(); 

var extractedText ;
var randomKeyWord ;

// OCR process starts from here
function extractText()
{    
    Tesseract.recognize
    (
        //'https://i2-prod.liverpoolecho.co.uk/incoming/article17096840.ece/ALTERNATES/s615/0_whatsappweb1_censored.jpg',
        'https://cdn.dribbble.com/users/1644453/screenshots/16718697/media/29c09b7e851274f2712a84c712060b2a.png?compress=1&resize=1600x1200&vertical=top',
        //'img.jpg',
        'eng',
        { logger: m => console.log(m) }
    )
    .then
    (({ data: { text } }) => 
        {
            extractedText = text;
            storeData();
        }
    )
}

function storeData()
{
    document.getElementById("text").innerHTML = extractedText;
    // extracted text to an array
    var textArray = extractedText.split(" ");
    console.log(textArray);

    // length of the extracted text
    console.log(textArray.length);

    // element storing array
    let randomNumbers = [];
    
    for (let i = 0; i < 5; i++) 
    {
        let randomNumber = Math.floor(Math.random() * textArray.length) + 1;
        // preventing number repitition
        while (randomNumbers.includes(randomNumber)) 
        {
            randomNumber = Math.floor(Math.random() * textArray.length) + 1;
        }
        randomNumbers.push(randomNumber);
        
        // selected text
        console.log(textArray[randomNumbers[i]]);       
    }
    console.log(randomNumbers);
}
