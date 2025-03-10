
from breakout import *
import os
from model import AtariNet
from agent import Agent
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

enviroment = DQNBreakout(device=device)

model = AtariNet(nb_action=4)

model.to(device)

model.load_the_model()

agent = Agent(model=model,
              device=device,
              epsilon=1.0,
              nb_warmup=5000,
              nb_actions=4,
              learning_rate=0.00001,
              memory_capacity=1000000,
              batch_size=64)

agent.train(env=enviroment, epochs=200000)
