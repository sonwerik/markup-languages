const add  = document.getElementById('add-task');
const taskContainer = document.getElementById('task-container');
const inputTask = document.getElementById('input-task');

addTask.addEventListener('click', function(){
    let task = document.createElement('div');
    task.classList.add('task');

    let li = document.createElement('li');
    li.innerText= `${inputTask.value}`;

    task.appendChild(li);

    let deleteButton = document.createElement("button");
    deleteButton.innerHTML = '<i class="fa-solid fa-check"></i>';
    deleteButton.classList.add('deleteTask');
    task.appendChild(deleteButton);

    if(inputTask.value === ""){
        alert('Si us plau introdueix una tasca.')
    } else {
        taskContainer.appendChild(task)
    }

    inputTask.value = "";

    checkButton.addEventListener('click', function(){
        checkButton.parentElement.style.textDecoration = 
        "line-throungh";
    });

    deleteButton.addEventListener('click', function(e){
        let target = e.target;
        target.parentElement.parentElement.remove();
    });

});