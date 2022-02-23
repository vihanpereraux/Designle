extractText(); 

var extractedText ;
var randomKeyWord ;

// OCR process starts from here
function extractText()
{    
    Tesseract.recognize
    (
        //'https://i2-prod.liverpoolecho.co.uk/incoming/article17096840.ece/ALTERNATES/s615/0_whatsappweb1_censored.jpg',
        'https://cdn.dribbble.com/users/6081502/screenshots/16571095/media/af2c1f5b9bb8f398560e412ce6a278fb.png?compress=1&resize=1600x1200&vertical=top',
        //'img/img.jpg',
        //'https://i.ibb.co/cX2QYFW/img3.jpg', 
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

    // saving randomNumbers[] in local storage
    localStorage.setItem("textArray", JSON.stringify(textArray));
    console.log("Extracted data saved in local storage");
}
