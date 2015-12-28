
# coding: utf-8

# In[1]:

days = ['Mon','Tue','Thr']
action = ['watch movie','reading','study']
list(zip(days,action))


# In[7]:

list(range(1,10,2))


# In[8]:

num_list = [num for num in range(1,6)]
num_list


# In[9]:

num_list = [num-1 for num in range(1,6)]
num_list


# In[11]:

num_list = [num-1 for num in range(1,6) if num %2 == 1]
num_list


# In[16]:

def hello_world():
    print('hello_world')


# In[17]:

hello_world()


# In[18]:

def colors(color):
    if color == 'red':
        return "it's red."
    elif color == 'blue':
        return "it's blue."


# In[20]:

colors('red')


# In[21]:

def print_arg(*arg):
    print('引數:',*arg)


# In[22]:

print_arg(233,2,33)


# In[ ]:



