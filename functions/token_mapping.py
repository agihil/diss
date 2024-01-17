"""
The function maps the character-indices to its tokenized version.
Input: Pandas Dataframe with the tokenized text, the original text (in string format), the name of the token column in the dataframe.
Output: Start Indices and End Indices of the tokens in the dataframe.
The function returns an Index Error when the Input doesnt correspond to the same text.
Requirements: pandas
"""
def map_tokens_to_indices(df, text, columnname):
    start_indices = []
    end_indices = []
    char_index = 0
    for index, row in df.iterrows():
        token = row[columnname]
        # Überprüfen, ob es das letzte Token im DataFrame ist
        if index != len(df) - 1:
            next_token = df[columnname].loc[index + 1]

            # Überprüfen, ob der Token im Text gefunden wurde
            if text[char_index:char_index + len(token)] == token:
                start_indices.append(char_index)
                end_indices.append(char_index+len(token)-1)
                char_index += len(token)

            # Finden der Größe des Zwischenraums
            while text[char_index] != next_token[0]:
                char_index += 1
        else:
            # Falls es das letzte Token ist, füge den aktuellen Index hinzu
            start_indices.append(char_index)
            end_indices.append(char_index+len(token)-1)
    return start_indices, end_indices

