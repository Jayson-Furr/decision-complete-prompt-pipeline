import { FormEvent, useMemo, useState } from "react";
import type { TodoItem } from "./types";

let nextTodoId = 1;

export default function App() {
  const [draft, setDraft] = useState("");
  const [todos, setTodos] = useState<TodoItem[]>([]);

  const remainingCount = useMemo(
    () => todos.filter((todo) => !todo.completed).length,
    [todos],
  );

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const text = draft.trim();
    if (!text) return;

    setTodos((current) => [
      ...current,
      { id: nextTodoId++, text, completed: false },
    ]);
    setDraft("");
  }

  function toggleTodo(id: number) {
    setTodos((current) =>
      current.map((todo) =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo,
      ),
    );
  }

  function deleteTodo(id: number) {
    setTodos((current) => current.filter((todo) => todo.id !== id));
  }

  return (
    <main className="app-shell" aria-labelledby="app-title">
      <section className="todo-card">
        <header className="todo-header">
          <p className="eyebrow">Local prototype</p>
          <h1 id="app-title">Tiny Tasks</h1>
          <p className="summary" aria-live="polite">
            {todos.length === 0
              ? "No tasks yet."
              : `${remainingCount} of ${todos.length} tasks remaining.`}
          </p>
        </header>

        <form className="todo-form" onSubmit={handleSubmit}>
          <label htmlFor="todo-input">New task</label>
          <div className="todo-entry-row">
            <input
              id="todo-input"
              value={draft}
              onChange={(event) => setDraft(event.target.value)}
              placeholder="Add a task"
              autoComplete="off"
            />
            <button type="submit">Add</button>
          </div>
        </form>

        {todos.length === 0 ? (
          <p className="empty-state">Add your first task to start the list.</p>
        ) : (
          <ul className="todo-list" aria-label="Todo list">
            {todos.map((todo) => (
              <li className="todo-item" key={todo.id}>
                <label className="todo-toggle">
                  <input
                    type="checkbox"
                    checked={todo.completed}
                    onChange={() => toggleTodo(todo.id)}
                  />
                  <span className={todo.completed ? "completed" : undefined}>
                    {todo.text}
                  </span>
                </label>
                <button type="button" onClick={() => deleteTodo(todo.id)}>
                  Delete
                </button>
              </li>
            ))}
          </ul>
        )}
      </section>
    </main>
  );
}
