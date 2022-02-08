// import Classifier from '/ml-classify-text';
const { Classifier } = require('ml-classify-text')

classifyText();


function classifyText()
{
    // classifier instance 
    const classifier = new Classifier();

    // default datasets
    let positive = [
        'This is great, so cool!',
        'Wow, I love it!',
        'It really is amazing',
    ]
     
    let negative = [
        'This is really bad',
        'I hate it with a passion',
        'Just terrible!',
    ]

    // training data
    classifier.train(positive, 'positive');
    classifier.train(negative, 'negative');

    // getting the prediction
    let predictions = classifier.predict('It sure is pretty great!')
 
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