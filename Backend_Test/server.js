const http = require('http');
const { Classifier } = require('ml-classify-text');
const { createWorker } = require('tesseract.js');

const server = http.createServer( (req, res) => 
{
    console.log("Working");
});

server.listen(3000, 'localhost', () => 
{
    console.log("listing");
    const classifier = new Classifier()

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
     
    classifier.train(positive, 'positive');
    classifier.train(negative, 'negative');

    let predictions = classifier.predict('It sure is pretty great!');
 
    if (predictions.length) 
    {
        predictions.forEach(prediction => 
        {
            console.log(`${prediction.label} (${prediction.confidence})`);
            console.log("Working2");
        })
    } 
    else 
    {
        console.log('No predictions returned');
    }


    const worker = createWorker();

    (async () => {
    await worker.load();
    await worker.loadLanguage('eng');
    await worker.initialize('eng');
    const { data: { text } } = await worker.recognize('https://tesseract.projectnaptha.com/img/eng_bw.png');
    console.log(text);
    await worker.terminate();
    })();
})