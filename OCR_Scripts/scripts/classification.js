function classifyText()
{

    let predictionText = document.getElementById("hero-text").textContent;

    var classifier;
    if (predictionText == 'crypto') 
    {
        // classifier instance 
        classifier = new Classifier({
            nGramMin: 2,
            nGramMax: 2
        });
    }

    if (predictionText == 'cryptozz') 
    {
        // classifier instance 
        classifier = new Classifier({
            nGramMin: 4,
            nGramMax: 4
        });
    }

    let tokens = classifier.tokenize('I really dont like it')

    console.log(tokens)

    // plant based dataset
    let plants = 
    [
        'tree',
        'plant',
        'coconut',
        'seeds',
        'green',
        'plantation',
        'garden',
        'I plant'
    ]
    
    // negative dataset
    let education = 
    [
        'lessons',
        'learn',
        'books',
        'tutorials',
        'books prices',
    ]

    let clothes = 
    [
        'dennim',
        'shirt',
        'clothes',
        'wear',
        'classy',
    ]

    let crypto = 
    [
        'bitcoin',
        'etherium',
        'nft',
        'generative',
        'blockchain',
        'I love',
    ]

    // training data
    classifier.train(plants, 'plantation');
    classifier.train(education, 'education');
    classifier.train(clothes, 'clothes');
    classifier.train(crypto, 'crypto');

    // getting the un-prediction text
    
    let predictions = classifier.predict('I love bitcoin money');

    let model = classifier.model;
    console.log(model.serialize());
 
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