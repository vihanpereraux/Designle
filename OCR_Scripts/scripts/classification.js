function classifyText()
{
    // classifier instance 
    const classifier = new Classifier();

    // plant based dataset
    let plantation = 
    [
        'tree',
        'plant',
        'coconut',
        'seeds',
        'green',
        'plantation',
        'garden'
    ]
    
    // negative dataset
    let negative = 
    [
        'This is really bad',
        'I hate it with a passion',
        'Just terrible!',
    ]

    // training data
    classifier.train(plantation, 'plantation');
    classifier.train(negative, 'negative');

    // getting the un-prediction text
    let predictionText = document.getElementById("hero-text").textContent;
    let predictions = classifier.predict(String(predictionText));
 
    // prediction starts
    if (predictions.length) 
    {
        predictions.forEach(prediction => 
        {
            console.log(`${prediction.label} (${prediction.confidence})`);
            
            // display results in the page
            document.getElementById("classified-text").innerHTML = 
                prediction.label + " " + prediction.confidence;
        })
    } 
    else 
    {
        console.log('No predictions returned');
    }
}