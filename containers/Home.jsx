import { Route, Routes } from "react-router-dom"
import { Counter, Footer,
         Navigation, TodoInput } from "../components"


const Home = () => {
    return (<>
            <table style={{ width: "600px", height: "600px", margin: "0 auto", border: "1px solid black"}}>
        <thead>
            <tr columns="3" >
                <td style={{ width: "100%", border: "1px solid black"}}><h3><Navigation/></h3></td>
            </tr>
        </thead>
        <tbody>
        <tr style={{ width: "20%",height: "80%",  border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <Routes>
                <Route path="/count" element={<Counter/>}></Route>
                <Route path="/todos/*" element={<TodoInput/>}></Route>
            </Routes>
            </td>
        </tr>
        <Footer/>
        </tbody>
    </table>
    </>)
}

export default Home