small_coords = defaultdict(list)
lati=[]
longi=[]
with open('USA-road-d.CAL.co', 'r') as f:
    for line in tqdm(f):
        if line[0]=='v':
            n, lat, long= list(map(int, line[2::].split()))
            small_coords[n]=[lat, long]
            lati.append(lat)
            longi.append(longi)
df = pd.DataFrame(small_coords).T
df.rename(columns={0:'latitude', 1:'longitude'}, inplace = True)
BBox = (df.longitude.min(),df.longitude.max(), df.latitude.min(), df.latitude.max())

coord = {node:{} for node in path}
for node in path: #path is the final path you have after the search
    coord[node]['latitude'] = small_coords[node][0]
    coord[node]['longitude'] = small_coords[node][1]

df2 = pd.DataFrame(coord).T
df2.rename(columns={1:'longitude', 0:'latitude'}, inplace = True)
mappa = plt.imread('mapNevada-Caliornia.png')
fig, ax = plt.subplots(figsize = (17,15))
ax.scatter(df2.longitude, df2.latitude, zorder=2, alpha= 0.5, c='b', s=1)
ax.set_title('Plotting Spatial Data')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(mappa, zorder=0, extent = BBox, aspect= 'equal')
