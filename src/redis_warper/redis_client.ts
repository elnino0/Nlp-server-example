import { createClient } from 'redis';
import config from "../config/appConfig";

export class redis_client {
    private static instance: redis_client;
    private client
    private isConnect : boolean = false;

    

    private constructor() {
        console.log(config)
        this.client = createClient({socket: {
            host: config.redisHost,
            port: config.redisPort
        },password: config.redisPass});
     }

    public static getInstance(): redis_client {
        if (!redis_client.instance) {
            redis_client.instance = new redis_client();
        }

        return redis_client.instance;
    }

    public async set(key:string,value:string){
        await this.connect()
        await this.client.set(key,value);
    }

    public async get(key:string){//yea you dont need async here , but its more clear .
        await this.connect()
        return this.client.get(key);
    }

    private async connect() {
        if (this.isConnect){
            return
        }

        await this.client.connect();
        this.isConnect = true
    }


    public async disconnect() {
        await this.client.disconnect();

    }
}

