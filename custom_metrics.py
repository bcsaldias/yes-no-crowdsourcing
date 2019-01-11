import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

class ListTable(list):
    def _repr_html_(self):
        html = ["<table>"]
        for row in self:
            html.append("<tr>")
            
            for col in row:
                html.append("<td>{0}</td>".format(col))
            
            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)
    
def draw_theta(theta, labels=None):
    """Draw the confusion matrix received.
    
    Parameters
    ----------
    theta : np.array
        confusion matrix drawn
    """     

    if labels is None:
        labels = []

    row_sums = theta.sum(axis=1)
    new_matrix = theta / row_sums[:, np.newaxis]
    print(np.round(new_matrix,3))
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    res = ax.imshow(new_matrix,  cmap=plt.cm.Blues, interpolation='nearest')
    plt.title('Confusion matrix\n')
    ticks = [i for i in range(len(theta))]
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    plt.ylabel('True Class')
    plt.xlabel('Predicted Class')
    plt.show()
    
def draw_metrics(y_true, y_pred, labels):
    """
    This method is only for to draw metrics
    
    """
    draw_theta(confusion_matrix(y_true, y_pred) , labels)
    table = ListTable()
    print("Acurracy score",accuracy_score(y_true, y_pred))
    table.append(["Metrics / Classes"]+list(labels))
    table.append(["Precision score"]+list(np.round(precision_score(y_true, y_pred, average=None),3)))
    table.append(["Recall score"]+list(np.round(recall_score(y_true, y_pred, average=None),3)))
    table.append(["F score"]+list(np.round(f1_score(y_true, y_pred, average=None),3)))
    return table

def metrics(y_true, y_pred):

    to_ret = {
            'p':precision_score(y_true, y_pred, average=None),
            'r':recall_score(y_true, y_pred, average=None),
            'f':f1_score(y_true, y_pred, average=None),
            }

    return to_ret

