import './App.css';
import { FC, useEffect, useState } from 'react';
import axios from 'axios';


type Todo = {
    id: number,
    title: string,
    body: string
};

const App: FC = () => {
    const [todos, setTodos] = useState<Todo[]>();

    useEffect(() => {
        axios.get('http://localhost:8000/api/'
        ).then(res => setTodos(res.data)
        ).catch(err => console.log(err))
    }, []);

    return (
        <div className="App">
            <div className="App-header">
                {
                    todos?.map((item: Todo) => {
                        return <TodoCard {...item} />
                    })
                }
            </div>
        </div>
    );
}

const TodoCard: FC<Todo> = ({ id, title, body }) => {
    const [showBody, setShowBody] = useState<boolean>(false);

    return (
        <div className="todo-card" key={id} onClick={(e) => setShowBody(!showBody)}>
            <h2>{title}</h2>
            {showBody && <p>{body}</p>}
        </div>
    );
}



export default App;
