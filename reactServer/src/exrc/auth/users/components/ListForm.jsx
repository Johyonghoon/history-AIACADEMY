export default function ListForm({list}){
    return <><h2>유저 목록</h2>
    <table className='user-list'>
        <thead>
            <tr>
            <th>user_id</th>
            <th>user_email</th>
            <th>password</th>
            <th>user_name</th>
            <th>phone</th>
            <th>birth</th>
            <th>address</th>
            <th>job</th>
            <th>user_interests</th>
            </tr>
        </thead>
        <tbody>
            {list && list.map((user) => (
                <tr key={user.id}>
                    <td>{user.user_id}</td>
                    <td>{user.user_email}</td>
                    <td>{user.password}</td>
                    <td>{user.user_name}</td>
                    <td>{user.phone}</td>
                    <td>{user.birth}</td>
                    <td>{user.address}</td>
                    <td>{user.job}</td>
                    <td>{user.user_interests}</td>
                </tr>
            ))}
        </tbody>
    </table>
    </>
}