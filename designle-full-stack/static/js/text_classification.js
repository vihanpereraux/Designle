function loadData()
{
    var savedPhrased = JSON.parse(localStorage.getItem('cleanedText'));
    console.log(savedPhrased[0]);
}


function classifyText()
{
    // classifier instance 
    var classifier = new Classifier ({
        nGramMin: 1,
        nGramMax: 1
    });

    // plants/garden based word bag
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
    
    // education/courses based word bag
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

    // fashion/clothing based word bag
    let clothes = 
    [
        'dennim',
        'shirt',
        'clothes',
        'wear',
        'classy',
    ]

    // crypto currency based word bag
    let crypto = 
    [
        'bitcoin',
        'etherium',
        'nft',
        'generative',
        'blockchain',
        'You love fff ttt',
    ]

    // train word bags according to the given configs
    classifier.train(plantation, 'plantation');
    classifier.train(education, 'education');
    classifier.train(clothes, 'clothes');
    classifier.train(crypto, 'crypto');

    // predict saved phrases
    let predictions = classifier.predict('plants');
    let model = classifier.model;
    console.log(model.serialize()); // details of the model
 
    var savedPhrased = JSON.parse(localStorage.getItem('cleanedText'));
    console.log(savedPhrased[0]);

    var results = []
    for (let i = 0; i < savedPhrased.length; i++) {

        let predictions = classifier.predict(savedPhrased[i]);

        // prediction starts
        if (predictions.length) 
        {
            predictions.forEach ( prediction => 
            {
                results.push(prediction.label)
                // console.log(`${prediction.label} (${prediction.confidence})`);
            })
        }
    }

    
    var modal = document.getElementById("myModal");
    var closeBtn = document.getElementById("closeBtn");
    var applyBtn = document.getElementById("applyBtn");
    var categoriesForm = document.getElementById("categories");
    var selectOptions = document.getElementById("categories");
    

    modal.style.display = "block";  
    
    for (let i = 0; i < results.length; i++) {
        var block = `<option value=${results[i]}>${results[i]}</option>` 
        selectOptions.innerHTML += block
    }
    
    closeBtn.onclick = function() {
        modal.style.display = "none";
    }

    applyBtn.onclick = function() {
        console.log(selectOptions.value);
        localStorage.setItem("category", JSON.stringify(selectOptions.value));
        modal.style.display = "none";
    }
    
    // console.log(results)
    // loadData()
}