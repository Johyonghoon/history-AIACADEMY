import Detail from "./user/Detail";
import FindEmail from "./user/FindEmail";
import FindPassword from "./user/FindPassword";
import GoogleLogin from "./user/GoogleLogin";
import List from "./user/List";
import Login from "./user/Login";
import Logout from "./user/Logout";
import RemoveUser from "./user/Remove";
import SignUp from "./user/SignUp";
import UpdateUser from "./user/Update";

export default function Home(){
    return (<>
    <table style={{ width: "1200px", height: "600px", margin: "0 auto", border: "1px solid black"}}>
        <thead>
            <tr>
                <td style={{ width: "100%", border: "1px solid black"}}>
                    {/* <Navigation/> */}
                </td>
            </tr>
        </thead>
        <tbody>
        <tr style={{ width: "20%", height: "80%",  border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <Login/>
            </td>
        </tr>
        <tr style={{ width: "100%", height: "20%", border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
                {/* <Footer/> */}
            </td>
        </tr>
        </tbody>
    </table>
    </>)
}
