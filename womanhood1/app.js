var express                  = require("express"),
    app                      = express(),
    bodyparser               = require("body-parser"),
    {spawn}                  = require('child_process');




app.use(bodyparser.urlencoded({extended:true}));
app.use('/public',express.static('public'));

app.set("view engine","ejs");
var dataToSend=""





app.get("/",function(req,res){
res.render("index",{data:dataToSend});
    
});


app.post("/",function(req,res){
const symptom1=req.body.symptom1;

var symptoms=symptom1;
console.log(symptoms);
  var dataToSend;
  // spawn new child process to call the python script
 
  const python = spawn('python', ['predictor_actual.py',symptoms]);
  // collect data from script
  python.stdout.on('data', function (data) {
   dataToSend = data.toString();
   console.log(dataToSend);
  
  
  });
  // in close event we are sure that stream from child process is closed
  python.on('close', (code) => {
  console.log(`child process close all stdio with code ${code}`);
  // send data to browser
  res.render("index",{data:dataToSend});
  });
})

app.get("/here",function(req,res){
  res.render("symptoms");
})


app.get("/pcos",function(req,res){
  var dataToSend=""

  res.render("pcos",{data:dataToSend})
});

app.post("/pcos",function(req,res){
  console.log(req.body.wake);
   var dataString=[req.body.optradio1,req.body.optradio2,req.body.optradio3,req.body.optradio4,req.body.optradio5,req.body.optradio6,req.body.optradio7,req.body.optradio8,req.body.optradio9,req.body.optradio10,req.body.optradio11,req.body.optradio12,req.body.sleep,req.body.wake,req.body.optradio13,req.body.optradio14,req.body.optradio15,req.body.optradio16,req.body.optradio17];
  // var dataString=req.body.optradio1+req.body.optradio2+req.body.optradio3+req.body.optradio4+req.body.optradio5+req.body.optradio6+req.body.optradio7+req.body.optradio8+req.body.optradio9+req.body.optradio10+req.body.optradio11+req.body.optradio12+req.body.sleep+req.body.wake+req.body.optradio13+req.body.optradio14+req.body.optradio15+req.body.optradio16+req.body.optradio17;

   console.log(dataString);
    var dataToSend;
    // spawn new child process to call the python script
   
    const python = spawn('python', ['PCOS_actual.py',JSON.stringify(dataString)]);
    // collect data from script
    python.stdout.on('data', function (data) {
     dataToSend = data.toString();
     console.log(dataToSend);
    
    
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    res.render("pcos",{data:dataToSend});
    });

});




let port=process.env.PORT;
if(port==null||port==""){
  port=2500;
}
app.listen(port, function () {
  console.log("Server started successfully at port 2500");
});
