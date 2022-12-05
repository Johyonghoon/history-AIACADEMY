import { Link } from "react-router-dom"

const Navigation = () => <nav>
    <ul>
        <li><Link to="/home">Home</Link></li>
        <li><Link to="/count">Counter</Link></li>
        <li><Link to="/todos">Todos</Link></li>
    </ul>   
</nav>

export default Navigation