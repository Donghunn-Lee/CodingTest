
function solution(id_list, report, k) {
    const userList = new Map();
    const restricted = [];
    
    for (let user of id_list) {
        userList.set(user, {receivedMail: 0, reportedFrom: new Set()});
    }
 
    for (let i = 0; i < report.length; i++) {
        const [user, reported] = report[i].split(" ");
        userList.get(reported).reportedFrom.add(user);
    }
    
    for (let user of id_list) {
        if (k <= userList.get(user).reportedFrom.size) {
            for (let reporter of userList.get(user).reportedFrom) {
                userList.get(reporter).receivedMail++;
            }
        }
    }
    
    for (let user of id_list) {
        restricted.push(userList.get(user).receivedMail);
    }
    
    return restricted;
}