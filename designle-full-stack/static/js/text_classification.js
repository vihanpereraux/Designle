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
    let products_option_one = 
    [
        'tropical', 'product', 'updates', 'shops', 'discounts', 'supplements', 'shop now', 'order', 'organic', 'customers',
        'oil', 'farms', 'original', 'source', 'newsletter', 'natural', 'nature', 'glow', 'glowing', 'makeup',
    ]
    let products_option_two = 
    [
        'look', 'tools', 'modern', 'style', 'personality', 'products', 'best', 'brands', 'learn more', 'better',
        'sleep', 'work', 'day', 'night', 'flavor', 'quality', 'unique', 'premium', 'energetic', 'worldwide',
    ]
    let products_option_three = 
    [
        'oil', 'farms', 'original', 'source', 'newsletter', 'natural', 'nature', 'glow', 'glowing', 'makeup',
        'happy', 'million', 'trending', 'shop', 'beauty', 'clean', 'drive', 'kits', 'wheels', 'eletronics',
    ]
    let products_option_four = 
    [
        'eco', 'farming', 'journey', 'hobby', 'cycling', 'bicyle', 'fish', 'bottle', 'water', 'sell',
        'winter', 'collection', 'fashionable', 'creative', 'classy', 'clothes', 'dress', 'baby', 'fashion', 'modern',
    ]
    let products_option_five = 
    [
        'collection', 'luxury', 'stylings', 'styles', 'your', 'speak', 'energy', 'bring', 'ideas', 'life',
        'quality', 'outfits', 'latest', 'heat', 'winter', 'summer', 'model', 'bag', 'hoodie', 'hoodies',
        'adidas', 'nike', 'boot', 'personal', 'elegant', 'shoes', 'arrivals', 'new', 'community', 'deliver',
        'tips', 'off', 'dressing', 'market', 'comfortable', 'natural', 'pro', 'aesthetic', 'shirt', 'shirts'
    ]
    
    // education/courses based word bag
    let ecommerce_bag_01 = 
    [
        'shopping', 'cart', 'services', 'purchase', 'credit', 'debit', 'selling', 'goods', 'shop', 'customer',
        'offers', 'seasonal', 'shopping', 'shop', 'change', 'order', 'start', 'add', 'filter', 'profile',
    ]
    let ecommerce_bag_02 = 
    [
        'faq', 'contact', 'ratings', 'more', 'products', 'rate', 'discount', 'price', 'stock', 'edition',
        'flash', 'deals', 'items', 'sold', 'seller', 'category', 'size', 'color', 'scan', 'collection',
    ]
    let ecommerce_bag_03 = 
    [
        'earn', 'buy', 'today', 'off', 'now', 'greatest', 'places', 'finest', 'view', 'all',
        'marketplace', 'find', 'search', 'explore', 'marketplace', 'social', 'sale', 'sales', 'best', 'brands',
    ]
    let ecommerce_bag_04 = 
    [
        'sold', 'out', 'you', 'interest', 'featured', 'language', 'english', 'china', 'wish', 'list',
        'register', 'coupen', 'purchase', 'over', 'now', 'claim', 'lkr', 'welcome', 'also', 'favourites',
    ]
    let ecommerce_bag_05 = 
    [
        'buyer', 'protection', 'sell on', 'more to love', 'browse', 'global', 'webiste', 'credit', 'debit', 'ali',
        'low', 'price', 'promotion', 'friday', 'black', 'great', 'value', 'customer services', 'reports', 'disputes',
    ]
    let ecommerce_bag_06 = 
    [
        'Intellectual Property Protection', 'Privacy Policy', 'Sitemap', 'Information for EU consumers', 'Transaction Services', 'User Information', 'Delivery', 'option', 'feedback', 'servey',
        'Partnerships', 'Collaborate', 'Shopping', 'Worldwide', 'islandwide', 'payment', 'Shop with confidence', 'Help center', 'Download', 'mobile',
    ]

    // fashion/clothing based word bag
    let financial_bag_01 = 
    [
        'information', 'about', 'us', 'bank', 'contact', 'money', 'financial', 'manage', 'salary', 'card',
        'report', 'interest', 'bonus', 'fraud', 'funds', 'expenses', 'earnings', 'invsesting', 'number', 'cvv',
    ]
    let financial_bag_02 = 
    [
        'income', 'wallet', 'digital', 'currency', 'balance', 'send', 'dollar', 'transactions', 'salary', 'save',
        'report', 'interest', 'payments', 'pay', 'details', 'activity', 'total', 'deposit', 'fixed', 'savings',
    ]
    let financial_bag_03 = 
    [
        'online', 'transactions', 'atm', 'withdraw', 'swip', 'pay', 'american express', 'investing', 'bill', 'members',
        'premium', 'holder', 'partner', 'mobile app', 'grow', 'apple pay', 'google pay', 'analytics', 'accounts', 'number',
    ]
    let financial_bag_04 = 
    [
        'crypto', 'bitcoin', 'etherium', 'decetralised', 'secure', 'protocol', 'solana', 'exchange', 'foreign', 'looping',
        'tokens', 'blocks', 'blockchain', 'trading', 'algorithmic', 'strategies', 'futurpe', 'passive', 'coin', 'bitmart',
    ]
    let financial_bag_05 = 
    [
        'generation', 'connect', 'top up', 'receive', 'send', 'stats', 'fee', 'convert', 'assets', 'nft',
        'collective', 'auctions', 'reliability', 'billions', 'millions', 'execution', 'laverage', 'economy', 'airdrop', 'track',
    ]

    // crypto currency based word bag
    let business_bag_01 = 
    [
        'products', 'brands', 'experience', 'work', 'build', 'client', 'projects', 'reviews', 'marketing', 'demo',
        'portfolio', 'software', 'industry', 'capital', 'venture', 'values', 'company', 'markets', 'airdrop', 'pricing',
    ]
    let business_bag_02 = 
    [
        'join', 'requirements', 'experience', 'business', 'community', 'expert', 'team', 'productive', 'founder', 'manage',
        'budget', 'demo', 'architect', 'ralse', 'marketing', 'agency', 'startup', 'brands', 'help', 'work',
    ]
    let business_bag_03 = 
    [
        'partners', 'success', 'tasks', 'digital', 'solutions', 'large', 'scale', 'create', 'raise', 'audience',
        'professional', 'technology', 'architect', 'flexible', 'afford', 'explore', 'come', 'estimate', 'meet', 'studio',
    ]


    // train word bags according to the given configs
    classifier.train(products_option_one, 'products option one');
    classifier.train(products_option_two, 'products option two');
    classifier.train(products_option_three, 'products option three');
    classifier.train(products_option_four, 'products option four');
    classifier.train(products_option_five, 'products option five');

    classifier.train(ecommerce_bag_01, 'ecommerce bag one');
    classifier.train(ecommerce_bag_02, 'ecommerce bag two');
    classifier.train(ecommerce_bag_03, 'ecommerce bag three');
    classifier.train(ecommerce_bag_04, 'ecommerce bag four');
    classifier.train(ecommerce_bag_05, 'ecommerce bag five');
    classifier.train(ecommerce_bag_06, 'ecommerce bag six');
    
    classifier.train(financial_bag_01, 'financial bag one');
    classifier.train(financial_bag_02, 'financial bag two');
    classifier.train(financial_bag_03, 'financial bag three');
    classifier.train(financial_bag_04, 'financial bag four');
    classifier.train(financial_bag_05, 'financial bag five');

    classifier.train(business_bag_01, 'business bag one');
    classifier.train(business_bag_02, 'business bag two');
    classifier.train(business_bag_03, 'business bag three');


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
                console.log(results)
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
    
    let cleanedResults = []
    for(let k = 0; k < results.length; k++){
        if(results[k].search("products") > -1){
            cleanedResults.push("products");
        }

        else if(results[k].search("ecommerce") > -1){
            cleanedResults.push("ecommerce");
        }

        else if(results[k].search("financial") > -1){
            cleanedResults.push("financial");
        }

        else if(results[k].search("financial") > -1){
            cleanedResults.push("business");
        }
    }
    cleanedResults = [...new Set(cleanedResults)];
    

    for (let i = 0; i < cleanedResults.length; i++) {
        var block = `<option value=${results[i]}>${cleanedResults[i]}</option>` 
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