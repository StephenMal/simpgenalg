

class basicViewer():

    __slots__ = ('debug')

    def __init__(self, debug = False):

        if not isinstance(debug, boolean):
            raise TypeError('Expected debug to be a boolean (True or False)')
        self.debug = debug

    @staticmethod
    def get_mean_and_CI(df, x, y, z=1.96):
        stats = df.groupby(x)[y].agg(['mean', 'count', 'std'])
        ci = [z*(row['std']/row['count']) for index, row in stats.iterrows()]
        return stats.index.tolist(), stats['mean'].tolist(), ci

    @staticmethod
    def _create_line_graph(df, x, y, clr):
        fig = go.Figure()
        if len(y) == 1 and clr is not None:
            groups = df.groupby(clr)
            for name in groups.groups.keys():
                c1, c2, c3 = random.randint(0,255),\
                             random.randint(0,255),\
                             random.randint(0,255)
                x_vals, means, ci = get_mean_and_CI(\
                                                groups.get_group(name), x, y[0])
                fig.add_trace(go.Scatter(x=x_vals, \
                                         y=means,\
                                         mode='lines', \
                                         name=name,\
                                         line_color=f'rgba({c1},{c2},{c3},1)',\
                                         showlegend=True,\
                                         error_y=dict(type='data',
                                                      array=ci,
                                                      visible=True)))
            return fig
        else:
            # Group by x-axis
            for y_indx, y_header in enumerate(y):
                c1, c2, c3 = random.randint(0,255),\
                             random.randint(0,255),\
                             random.randint(0,255)

                x_vals, means, ci = get_mean_and_CI(df, x, y_header)
                fig.add_trace(go.Scatter(x=x_vals, \
                                         y=means,\
                                         mode='lines', \
                                         name=y_header,\
                                         line_color=f'rgba({c1},{c2},{c3},1)',\
                                         showlegend=True,\
                                         error_y=dict(
                                                type='data',
                                                array=ci,
                                                visible=True)))
            return fig
