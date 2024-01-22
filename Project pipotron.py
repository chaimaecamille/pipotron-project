#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_pipotron(p_size, list_possibilities, sentence):
    # Split the sentence into components based on spaces and punctuation
    components = sentence.split()
    
    # Check if the number of components matches the specified pipotron size
    if len(components) != p_size:
        return False
    
    # For each component check if it belongs to the corresponding set of possibilities in the list of possibilities
    for i in range(p_size - 1):
        if components[i] not in list_possibilities[i + 1]:
            return False
    
    # Check if the last component is a punctuation
    last_component = components[-1]
    if last_component not in list_possibilities[p_size]:
        return False
    
    return True


# In[2]:


# Test the function with the example
p_size = 3
dict_possibilities = {
    1: ['Je', 'Tu', 'Demain je'],
    2: ['mange', 'bois', 'vole', 'voles'],
    3: ['.', '!', '?', '...']
}

sentence_1 = 'Je mange !'
sentence_2 = 'Tu dors ?'

result_1 = is_pipotron(p_size, dict_possibilities, sentence_1)
result_2 = is_pipotron(p_size, dict_possibilities, sentence_2)

(result_1, result_2)


# In[ ]:




