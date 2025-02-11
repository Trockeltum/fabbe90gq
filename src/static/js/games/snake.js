window.onload = function () {
    (function(){
    var canvas = document.getElementById("game-layer");
    var canvasLeft = canvas.offsetLeft + canvas.clientLeft;
    var canvasTop = canvas.offsetTop + canvas.clientTop;
    var ctx = canvas.getContext("2d");

    var deadtail;
    var newhead;
    var fruit;
    var snake;
    var key;
    var oldkey;
    var started;
    var deadval;
    var speed;

    ready();
    function ready(){
        snake = [[20,20]];
        key = 'none';
        oldkey = 'none';
        started = false;
        deadval = false;
        speed = 550;

        ctx.fillStyle = 'black';
        ctx.fillRect(0, 0, 500, 300);

        ctx.beginPath();
        ctx.fillStyle = 'yellow';
        ctx.fillRect(20, 20, 10 , 10);

        spawnFruit(snake);

    }



    // runs game
    function gameLoop() {
        console.log("gameLoop", speed, deadval);
        console.log("snake lenght", snake.length);
        console.log(key);
        move(snake,key);
        eaten(snake,fruit);
        drawhead(newhead);
        undrawtail(deadtail);
        oldkey = key;
        if (deadval){
            return;
        };
        setTimeout(gameLoop, speed/10);
    }
  
    // listens for the key
    document.addEventListener('keydown', (event) => {
        console.log("PRESSED KEYup", event.key, key, oldkey);
        if (key != oldkey){
            return
        }
        if (event.key == 'd' || event.key == 'a' || event.key == 'w' || event.key == 's'){
            if (event.key != oldkey){
                key = event.key;}
        } else{
            console.log('other kwy pressed: ', key)
        }
        if (!started){
            gameLoop() // 33 milliseconds = ~ 30 frames per sec
            console.log('started gameloop')

            started = true;
        }
    });

    // stops game loop and shows end screen
    function dead(){
        deadval = true;
        document.getElementById("leaderboard").style.display = "block";
        ctx.font = "30px Arial";
        ctx.fillStyle = "purple";
        ctx.fillText('Dead', 200,150)

    };

    // calculates new position
    // checks if snake has run into itself or wall
    function move(snake, key){
        console.log("move key:", key);
        console.log("old snake: ", snake);
        console.log('last: ',snake[snake.length - 1]);
        if (snake[snake.length - 1][0] === 0 || snake[snake.length - 1][0] === canvas.width || snake[snake.length - 1][1] === 0 || snake[snake.length - 1][1] === canvas.height ){
            console.log('went into wall');
        };
        if (key=="d"){
            newhead= [snake[snake.length - 1][0] + 10,snake[snake.length - 1][1]] 
        };
        if (key=="a"){
            newhead = [snake[snake.length - 1][0] - 10,snake[snake.length - 1][1]]
        };
        if (key=="w"){
            newhead = [snake[snake.length - 1][0],snake[snake.length - 1][1] - 10]
        };
        if (key=="s"){
            newhead = [snake[snake.length - 1][0],snake[snake.length - 1][1] + 10]
        };

        console.log("new head: ", newhead);
        for (var i = 0 ; i <snake.length; i++){
            if (newhead[0] == snake[i][0] && newhead[1] == snake[i][1]){
                console.log('move: ran into yourself');
                dead();
                return;
            }else if(newhead[0] < 0 || newhead[0] > 490 || newhead[1] < 0 || newhead[1] > 290){
                console.log('move: ran into wall');
                dead();
                return;
            }
        };
        snake.push(newhead);
        console.log(newhead)
        deadtail = snake.shift();
        console.log("new snake: ", snake);
    };
    // to place a fruit outside of snake
    function spawnFruit(snake){
        console.log('spawnfruit')
        while(true){
            let x = Math.round(Math.random()*(canvas.width-10)/10)*10
            let y =  Math.round(Math.random()*(canvas.height-10)/10)*10
            console.log('spawnfruitloop', x, y)
            var valid = true

            // check if in snake
            for(var i = 0; i < snake.length; i++){
                if (x == snake[i][0] && y == snake[i][1]){
                    console.log('spawnfruit: in snake not valid')
                    var valid = false
                };
            };

            // places fruit if it valid otherwise go another round
            if(valid){
                ctx.beginPath();
                ctx.fillStyle = 'red';
                console.log('fillreact', x, y)
                ctx.fillRect(x, y, 10 , 10);
                fruit = [x,y]
                break
            };
        };
    };
    // checks if snake head is on fruit
    function eaten(snake, fruit){
        console.log('eaten', snake[snake.length-1][0], fruit[0], snake[snake.length-1][1], fruit[1])
        if (snake[snake.length-1][1] === fruit[1] && snake[snake.length-1][0] === fruit[0]){
            console.log('eaten: feruit has eaten');
            spawnFruit(snake[0]);
            snake.unshift(snake[0]);
            snake.unshift(snake[0]);
            snake.unshift(snake[0]);
            speed -= 1;
            var scoreElement = document.getElementById('score');
            scoreElement.innerHTML = 'Score: ' + snake.length.toString()+ ' Speed: ' + speed;
        };
    };

    // paints the new head
    function drawhead(newhead){
        ctx.beginPath();
        ctx.fillStyle = 'yellow';
        ctx.fillRect(newhead[0], newhead[1], 10 , 10);

    };

    // unpaints the tail
    function undrawtail(deadtail){
        ctx.beginPath();
        ctx.fillStyle = 'black';
        ctx.fillRect(deadtail[0], deadtail[1], 10 , 10);

    };
    document.getElementById("resetbutton").addEventListener("click", function (event) {

        var scoreElement = document.getElementById('score');
        scoreElement.innerHTML = 'Score: 0';
       
        document.getElementById("game-layer").style.display = "block";
        document.getElementById("leaderboard").style.display = "none";
            

        ready();

    });
    
    
        
    })();
};
