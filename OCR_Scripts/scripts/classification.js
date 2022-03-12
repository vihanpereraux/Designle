function classifyText()
{

    let predictionText = document.getElementById("hero-text").textContent;

    var classifier;
    if (predictionText == 'crypto') 
    {
        // classifier instance 
        classifier = new Classifier({
            nGramMin: 1,
            nGramMax: 1
        });
    }

    //console.log(tokens)

    // plant based dataset
    let plantation = 
    [
        'The easiest way to make healthy life by buying favourite plants', 
        'Look natural with plantings',
        'Loved by gardens and trusted by gardners',
        'Save the earth with plants',
        'Growing beautiful plants at home has never been easier',
        'Delivering plants with hapiness',
        'One with nature',
        'Plants make life better',
        'Proper greening and smart solutions',
        'Bring calm to your place with interior plants',
        'Healthy plants garden and home',
        'We take care of your garden and flowers',
        'Plants for your interior',
        'Plant makes everything better',
        'Decorate your garden with plants',
        'Home is where my plants are',
        'Shop rare plants with plants collection',
        'Drops on leaves',
        'Create your urben jungle',
        'Plants and gardening for everyone'
    ]
    
    // negative dataset
    let education = 
    [
        'learning makes me happy',
        'getting you where you want to study',
        'a way to improve your skills',
        'online education is now easy',
        'build better assignments',
        'schools are closed learning is open',
        'better future for your kids',
        'study from home with experts',
        'welcome to private university',
        'grow your skills to advance your career path',
        'the best online course',
        'a new way to improve your skills',
        'improve your skills faster',
        'you can learn anything',
        'your mobile education',
        'education', 
        'tutorials', 
        'courses', 
        'course',
        'new way of learning'
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
        'You love fff ttt',
    ]

    // training data
    classifier.train(plantation, 'plantation');
    classifier.train(education, 'education');
    classifier.train(clothes, 'clothes');
    classifier.train(crypto, 'crypto');

    // getting the un-prediction text
    
    let predictions = classifier.predict('plant');

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