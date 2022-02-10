function classifyText()
{
    // classifier instance 
    const classifier = new Classifier();

    // default datasets
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
    
    let negative = 
    [
        'This is really bad',
        'I hate it with a passion',
        'Just terrible!',
    ]

    // training data
    classifier.train(plantation, 'plantation');
    classifier.train(negative, 'negative');

    // getting the prediction
    let predictionText = document.getElementById("hero-text").textContent;
    console.log(predictionText);
    let predictions = classifier.predict(String(predictionText));
 
    if (predictions.length) 
    {
        predictions.forEach(prediction => 
        {
            console.log(`${prediction.label} (${prediction.confidence})`);
            document.getElementById("classified-text").innerHTML = 
                prediction.label + " " + prediction.confidence;
        })
    } 
    else 
    {
        console.log('No predictions returned');
    }
}