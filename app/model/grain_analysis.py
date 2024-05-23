from math import pi,sqrt
import matplotlib.pyplot as plt
import segmenteverygrain as seg 

class GrainAnalysis:
    def __init__(self):
        self.id = None

    def update_grain_data(self,grain_data, scale):

        def calc_ri(a):
            r = sqrt(a/pi)
            ri=2*pi*r
            return ri

        def calculate_shape_from_size(size):
            ranges_in_mm = [0.0039, 0.063,0.125,0.250,0.5, 1.0, 2.0,4.0,8.0,16.0,32.0,64.0, 256.0]
            sorted_particles = {}

            if size<ranges_in_mm[0]:
                return 'clay'
            elif (size < ranges_in_mm[1]) & (size > ranges_in_mm[0]):
                return 'silt'
            elif (size < ranges_in_mm[2]) & (size > ranges_in_mm[1]):
                return 'very fine sand'
            elif (size < ranges_in_mm[3]) & (size > ranges_in_mm[2]):
                return 'fine sand'
            elif (size < ranges_in_mm[4]) & (size > ranges_in_mm[3]):
                return 'medium sand'
            elif (size < ranges_in_mm[5]) & (size > ranges_in_mm[4]):
                return 'coarse sand'
            elif (size < ranges_in_mm[6]) & (size > ranges_in_mm[5]):
                return 'sand'
            elif (size < ranges_in_mm[7]) & (size > ranges_in_mm[6]):
                return 'very fine gravel'
            elif (size < ranges_in_mm[8]) & (size > ranges_in_mm[7]):
                return 'fine gravel'
            elif (size < ranges_in_mm[9]) & (size > ranges_in_mm[8]):
                return 'medium gravel'
            elif (size < ranges_in_mm[10]) & (size > ranges_in_mm[9]):
                return 'coarse gravel'
            elif (size < ranges_in_mm[11]) & (size > ranges_in_mm[10]):
                return 'gravel'
            elif (size < ranges_in_mm[12]) & (size > ranges_in_mm[11]):
                return 'cobbles'
            elif (size > ranges_in_mm[12]):
                return 'boulder'

        grain_data['major_axis_length(mm)'] = grain_data['major_axis_length'].values*scale
        grain_data['minor_axis_length(mm)'] = grain_data['minor_axis_length'].values*scale
        grain_data['perimeter(mm)'] = grain_data['perimeter'].values*scale
        grain_data['area(mm)'] = grain_data['area'].values*scale**2
        grain_data['Roundness Index'] = grain_data['area'].apply(calc_ri)
        grain_data['Elongation Index'] = grain_data.apply(lambda row: (row['major_axis_length'] - row['minor_axis_length']) / row['major_axis_length'], axis=1)
        grain_data['shape'] = grain_data.apply(lambda row: calculate_shape_from_size(row['perimeter(mm)']),axis=1)
        grain_data['circularity']=grain_data.apply(lambda row : (4*row['area(mm)']*pi) / row['perimeter(mm)']**2, axis=1 )
        grain_data['elongation'] =grain_data.apply(lambda row : sqrt((row['major_axis_length']**2/row['minor_axis_length']**2)), axis=1)
        grain_data['compactness'] = grain_data.apply(lambda row: sqrt((4*row['area(mm)'] / pi * row['major_axis_length(mm)']**2 )), axis=1 )
        
        return grain_data

    def plot_image_w_shape_color(image, all_grains, ax, grain_data, cmap='viridis'):
        shapes = grain_data['shape'].unique()
        colors = {
            'clay': 'brown',
            'silt': 'grey',
            'very fine sand': 'yellow',
            'fine sand': 'blue',
            'medium sand': 'orange',
            'coarse sand': 'pink',
            'sand': 'purple',
            'very fine gravel': 'red',
            'fine gravel': 'green',
            'medium gravel': 'cyan',
            'coarse gravel': 'magenta',
            'gravel': 'lime',
            'cobbles': 'navy',
            'boulder': 'teal'
            }
        plotted_shapes = set()  # Keep track of shapes that have been plotted
        ax.imshow(image)
        for i in range(len(all_grains)):
            shape=grain_data.iloc[i]['shape']
            #color_idx = np.where(shapes == shape)[0][0]
            #print(color_idx)
            color = colors[shape]
            label = shape if shape not in plotted_shapes else ""
            centroid = all_grains[i].centroid
            ax.fill(all_grains[i].exterior.xy[0], all_grains[i].exterior.xy[1],
                    facecolor=color, edgecolor='none', linewidth=1, alpha=0.4, label=label)
            ax.plot(all_grains[i].exterior.xy[0], all_grains[i].exterior.xy[1],
                    color='k', linewidth=1)
            #plt.text(centroid.x, centroid.y, str(int(grain_data.iloc[i]['perimeter(mm)']))  , ha='right', va='top', color="red", fontsize=15)
            plotted_shapes.add(shape)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.legend()

    def PSD(grain_data, save=None, show=True):
        psd = plt.figure()

        sizes = grain_data['perimeter(mm)'].apply(int)
        #hist, bins = np.histogram(sizes, bins=7)
        plt.hist(sizes ,density=False, cumulative=False, histtype="bar", edgecolor='black')
        plt.xlabel('Particle perimeter(mm)')
        plt.ylabel('Frequency')
        plt.title('Particle Shape Distribution')
        if save is not None:
            psd.savefig(save)
        plt.grid(True)
        if show:
            plt.show()


    def PCD(grain_data,save=None):
        psd = plt.figure()
        circularity = grain_data['circularity']
        plt.hist(circularity, density=True,  edgecolor='black')
        plt.xlabel('Particle circularity')
        plt.ylabel('Frequency')
        plt.title('Particle circularity Distribution')
        plt.grid(True)
        if save is not None:
            psd.savefig(save)
    #plt.show()

    def show_segmentation_result(self,original_image,all_grains,labels,mask_all,grain_data,fig,ax):
        outputfig, ax = plt.subplots(figsize=(8,8))
        ax.imshow(original_image)
        self.plot_image_w_shape_color(original_image, all_grains, ax, grain_data, cmap='viridis')
        seg.plot_grain_axes_and_centroids(all_grains, labels, ax, linewidth=1, markersize=10)

