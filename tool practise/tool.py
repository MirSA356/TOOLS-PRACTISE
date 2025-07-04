from agents import Agent, Runner
from main import config

agent = Agent(
    name='General Agent',
    instructions=" You Are A HelpFull Assistant. Your task is a help the user with their queries"
)

result = Runner.run_sync(agent,
                         'who is the founder of pakistan?',
                        run_config=config)

print(result.final_output)

#ye sirf porani chezen batata hai. real time data nhi batata or personal data bhi nhi batata
