import * as dotenv from 'dotenv';
dotenv.config();

function tryIntPrase(str:string){
    const num = Number(process.env.REDIS_PORT);
    if(isNaN(num)){
        return undefined;
    }

    return num;
}

export default {
    UserUrl: process.env.USER_SERVICE_URL ?? 'http://127.0.0.1:5000/analyze',
    redisPass: process.env.REDIS_PASS ?? '1234',
    redisHost: process.env.REDIS_HOST ?? "localhost",
    redisPort:  tryIntPrase(process.env.REDIS_PORT) ?? 6379
   }
