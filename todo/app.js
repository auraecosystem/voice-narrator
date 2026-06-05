// Simple To-Do app with localStorage persistence
const STORAGE_KEY = 'todos-v1';

let todos = [];
let filter = 'all'; // all | active | completed

// Elements
const form = document.getElementById('todo-form');
const input = document.getElementById('todo-input');
const list = document.getElementById('todo-list');
const countEl = document.getElementById('count');
const filters = document.querySelectorAll('.filter');
const clearBtn = document.getElementById('clear-completed');

function save() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(todos));
}

function load() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    todos = raw ? JSON.parse(raw) : [];
  } catch (e) {
    console.error('Failed to load todos', e);
    todos = [];
  }
}

function createTodo(text) {
  return { id: Date.now().toString(), text: text.trim(), completed: false };
}

function addTodo(text) {
  if (!text.trim()) return;
  todos.unshift(createTodo(text));
  save();
  render();
  input.value = '';
  input.focus();
}

function updateTodo(id, fields) {
  const i = todos.findIndex(t => t.id === id);
  if (i === -1) return;
  todos[i] = { ...todos[i], ...fields };
  save();
  render();
}

function removeTodo(id) {
  todos = todos.filter(t => t.id !== id);
  save();
  render();
}

function clearCompleted() {
  todos = todos.filter(t => !t.completed);
  save();
  render();
}

function setFilter(f) {
  filter = f;
  filters.forEach(b => b.classList.toggle('active', b.dataset.filter === f));
  render();
}

function filteredTodos() {
  if (filter === 'active') return todos.filter(t => !t.completed);
  if (filter === 'completed') return todos.filter(t => t.completed);
  return todos;
}

function render() {
  list.innerHTML = '';
  const items = filteredTodos();
  if (items.length === 0) {
    const empty = document.createElement('li');
    empty.className = 'todo-item';
    empty.textContent = 'No tasks';
    list.appendChild(empty);
  } else {
    for (const todo of items) {
      const li = document.createElement('li');
      li.className = 'todo-item';
      li.dataset.id = todo.id;

      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.checked = todo.completed;
      checkbox.className = 'toggle';
      checkbox.setAttribute('aria-label', 'Toggle complete');

      const text = document.createElement('div');
      text.className = 'todo-text' + (todo.completed ? ' completed' : '');
      text.textContent = todo.text;
      text.tabIndex = 0;
      text.setAttribute('role','textbox');
      text.setAttribute('aria-label','Todo text');

      const actions = document.createElement('div');
      actions.className = 'actions';

      const editBtn = document.createElement('button');
      editBtn.className = 'action-btn edit';
      editBtn.title = 'Edit';
      editBtn.innerHTML = '✏️';

      const delBtn = document.createElement('button');
      delBtn.className = 'action-btn delete';
      delBtn.title = 'Delete';
      delBtn.innerHTML = '🗑️';

      actions.appendChild(editBtn);
      actions.appendChild(delBtn);

      li.appendChild(checkbox);
      li.appendChild(text);
      li.appendChild(actions);

      list.appendChild(li);
    }
  }

  const remaining = todos.filter(t => !t.completed).length;
  countEl.textContent = `${remaining} item${remaining !== 1 ? 's' : ''} left`;
}

// Event listeners
form.addEventListener('submit', (e) => {
  e.preventDefault();
  addTodo(input.value);
});

list.addEventListener('click', (e) => {
  const li = e.target.closest('.todo-item');
  if (!li) return;
  const id = li.dataset.id;

  if (e.target.matches('.toggle')) {
    updateTodo(id, { completed: e.target.checked });
    return;
  }

  if (e.target.closest('.delete')) {
    removeTodo(id);
    return;
  }

  if (e.target.closest('.edit')) {
    startEditing(li, id);
    return;
  }
});

// allow double-click text to edit
list.addEventListener('dblclick', (e) => {
  const li = e.target.closest('.todo-item');
  if (!li) return;
  const id = li.dataset.id;
  startEditing(li, id);
});

filters.forEach(btn => {
  btn.addEventListener('click', () => setFilter(btn.dataset.filter));
});

clearBtn.addEventListener('click', () => {
  clearCompleted();
});

// Inline edit helper
function startEditing(li, id) {
  const todo = todos.find(t => t.id === id);
  if (!todo) return;
  const textEl = li.querySelector('.todo-text');
  const inputEl = document.createElement('input');
  inputEl.className = 'edit-input';
  inputEl.value = todo.text;
  li.replaceChild(inputEl, textEl);
  inputEl.focus();
  inputEl.select();

  function finish(saveFlag) {
    const newText = inputEl.value.trim();
    if (saveFlag && newText) updateTodo(id, { text: newText });
    else render();
    cleanup();
  }

  function onKey(e) {
    if (e.key === 'Enter') finish(true);
    if (e.key === 'Escape') finish(false);
  }

  function cleanup() {
    inputEl.removeEventListener('blur', onBlur);
    inputEl.removeEventListener('keydown', onKey);
  }

  function onBlur() { finish(true); }

  inputEl.addEventListener('blur', onBlur);
  inputEl.addEventListener('keydown', onKey);
}

// Initialize
load();
render();
