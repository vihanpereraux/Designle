function classifyText()
{
    // classifier instance 
    const classifier = new Classifier();

    // default datasets
    let greenery = [
        'Tree',
        'Leaves',
        'Planting',
        'Plants',
    ]
     
    let negative = [
        'This is really bad',
        'I hate it with a passion',
        'Just terrible!',
    ]

    // training data
    classifier.train(greenery, 'greenery');
    classifier.train(negative, 'negative');

    // getting the prediction
    let predictions = classifier.predict('Plants World')
 
    if (predictions.length) 
    {
        predictions.forEach(prediction => 
        {
            console.log(`${prediction.label} (${prediction.confidence})`);
        })
    } 
    else 
    {
        console.log('No predictions returned');
    }
}