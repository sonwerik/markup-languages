const addTask = document.getElementById('add-task');
const taskContainer = document.getElementById('task-container');
const inputTask = document.getElementById('input-task');

addTask.addEventListener('click', function () {
    let task = document.createElement('div');
    task.classList.add('task');

    let li = document.createElement('li');
    li.innerText = `${inputTask.value}`;
    task.appendChild(li);

    let checkButton = document.createElement("button");
    checkButton.innerHTML = '<i class="fa-solid fa-check"></i>';
    checkButton.classList.add('checkTask');
    task.appendChild(checkButton);

    let deleteButton = document.createElement("button");
    deleteButton.innerHTML = '<i class="fa-solid fa-trash"></i>';
    deleteButton.classList.add('deleteTask');
    task.appendChild(deleteButton);

    if (inputTask.value === "") {
        alert('Si us plau introdueix una tasca.');
    } else {
        taskContainer.appendChild(task);
    }

    inputTask.value = "";

    checkButton.addEventListener('click', function () {
        if (li.style.textDecoration === "line-through") {
            li.style.textDecoration = "none";
        } else {
            li.style.textDecoration = "line-through";
        }
        checkButton.classList.toggle('completed');
    });

    deleteButton.addEventListener('click', function () {
        task.remove();
    });
});