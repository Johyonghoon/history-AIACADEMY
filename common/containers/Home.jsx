import { Route, Routes } from "react-router-dom"
import { Schedule } from "todos"
import { Counter, Footer, Navigation } from "common"
import { Login, SignUp } from "auth"

const Home = () => {
    return (<>
    <table style={{ width: "600px", height: "600px", margin: "0 auto", border: "1px solid black"}}>
        <thead>
            <tr columns="3" >
                <td style={{ width: "100%", border: "1px solid black"}}>
                    <Navigation/>
                </td>
            </tr>
        </thead>
        <tbody>
        <tr style={{ width: "20%", height: "80%",  border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <Routes>
                <Route path="/count" element={<Counter/>}></Route>
                <Route path="/todos" element={<Schedule/>}></Route>
                <Route path="/signup" element={<SignUp/>}></Route>
                <Route path="/login" element={<Login/>}></Route>
            </Routes>
            </td>
        </tr>
        <tr style={{ width: "100%", height: "20%", border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
                <Footer/>
            </td>
        </tr>
        </tbody>
    </table>
    </>)
}

export default Home