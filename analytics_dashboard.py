
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
innovations_df = pd.read_csv('/Users/user/Downloads/Enhanced_Idea_Development_Data_Platform_MySQL/data/innovations.csv')
students_df = pd.read_csv('/Users/user/Downloads/Enhanced_Idea_Development_Data_Platform_MySQL/data/students.csv')
investors_df = pd.read_csv('/Users/user/Downloads/Enhanced_Idea_Development_Data_Platform_MySQL/data/investors.csv')

# Merge innovations with students data
merged_data = pd.merge(innovations_df, students_df, on="student_id", how="left")

# Ensure output directory exists
os.makedirs('Sample_Output', exist_ok=True)

# ---- Enhanced Histogram: Number of projects per student -----------------------------
sns.set_theme(style="whitegrid")
plt.figure(figsize=(19.2, 10.8))

# Calculate project counts per student
project_counts = innovations_df['student_id'].value_counts()

# Use Seaborn’s built-in styling for modern design
sns.histplot(project_counts, bins=10, kde=True, color='#2E86C1', edgecolor='black')

# Title and labels with enhanced font
plt.title('Distribution of Number of Projects Submitted per Student', fontsize=22, fontweight='bold', pad=25)
plt.xlabel('Number of Projects', fontsize=18)
plt.ylabel('Number of Students', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Add annotation text for clarity
plt.text(project_counts.mean(), plt.ylim()[1]*0.9,
         f"Average Projects: {project_counts.mean():.1f}",
         fontsize=16, color='black', fontweight='bold')

# Grid, theme, and borders
sns.despine(left=True, bottom=True)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Save high-quality version
plt.tight_layout()
plt.savefig('Sample_Output/enhanced_histogram_projects_per_student.png', dpi=300, bbox_inches='tight')
plt.show()

# Set modern, clean visual style
sns.set_style("whitegrid")
sns.set_palette("crest")

plt.figure(figsize=(19.2, 10.8))
bars = merged_data['department'].value_counts().plot(kind='bar', color=sns.color_palette("crest", 5))

# Add title and labels with professional formatting
plt.title('Number of Innovation Projects by Department', fontsize=20, fontweight='bold', pad=20)
plt.xlabel('Department', fontsize=16)
plt.ylabel('Number of Projects', fontsize=16)
plt.xticks(rotation=45, fontsize=13)
plt.yticks(fontsize=12)

# Add value labels above each bar
for p in bars.patches:
    plt.text(p.get_x() + p.get_width()/2, p.get_height() + 1,
             int(p.get_height()), ha='center', fontsize=13, fontweight='bold', color='#2E4053')

# Add subtle background and frame styling
sns.despine(left=True, bottom=True)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('Sample_Output/enhanced_bar_projects_per_department.png', dpi=300)
plt.show()

# ---- Enhanced Count Plot: Submissions per University vs Category ------------------------------

sns.set_theme(style="whitegrid")
plt.figure(figsize=(19.2, 10.8))

# Create the enhanced count plot
ax = sns.countplot(
    data=merged_data,
    x='university',
    hue='category',
    palette='crest',        # elegant gradient palette
    edgecolor='black',
    linewidth=1.2
)

# Enhanced title and labels
plt.title('Number of Innovation Projects per University by Category', fontsize=22, fontweight='bold', pad=25)
plt.xlabel('University', fontsize=18)
plt.ylabel('Number of Projects', fontsize=18)
plt.xticks(fontsize=14, rotation=15)
plt.yticks(fontsize=13)

# Add value labels on top of each bar
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', fontsize=12, padding=2, color='black', fontweight='bold')

# Legend styling
plt.legend(
    title='Category',
    title_fontsize=14,
    fontsize=12,
    bbox_to_anchor=(1.02, 1),
    loc='upper left',
    borderaxespad=0,
    frameon=True
)

# Clean up grid and frame
sns.despine(left=True, bottom=True)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Save high-resolution output
plt.tight_layout()
plt.savefig('Sample_Output/enhanced_countplot_university_vs_category.png', dpi=300, bbox_inches='tight')
plt.show()

# ---- Enhanced Heatmap: Correlation between Submission Date and Project Category -----------------

# Convert submission_date to datetime
innovations_df['submission_date'] = pd.to_datetime(innovations_df['submission_date'], errors='coerce')

# Create month names for better readability
innovations_df['month_name'] = innovations_df['submission_date'].dt.strftime('%b')

# Create crosstab (month vs category)
submission_category_correlation = pd.crosstab(
    innovations_df['month_name'],
    innovations_df['category']
)

# Set Seaborn theme
sns.set_theme(style="whitegrid")

# Plot the enhanced heatmap
plt.figure(figsize=(19.2, 10.8))
ax = sns.heatmap(
    submission_category_correlation,
    annot=True,
    fmt='d',
    cmap='coolwarm',
    linewidths=0.5,
    linecolor='white',
    cbar_kws={'label': 'Number of Projects'}
)

# Title and labels
plt.title('Innovation Submissions by Month and Category', fontsize=22, fontweight='bold', pad=25)
plt.xlabel('Project Category', fontsize=18)
plt.ylabel('Submission Month', fontsize=18)

# Axis label font sizes
plt.xticks(fontsize=14, rotation=30, ha='right')
plt.yticks(fontsize=14, rotation=0)

# Add grid and layout
sns.despine(left=True, bottom=True)
plt.tight_layout()

# Save high-resolution version
plt.savefig('Sample_Output/enhanced_heatmap_submission_date_vs_category.png', dpi=300, bbox_inches='tight')
plt.show()

# ---- Enhanced Pair Plot: Relationships between multiple numerical variables --------------

# Convert dates and extract useful numerical features
innovations_df['submission_date'] = pd.to_datetime(innovations_df['submission_date'], errors='coerce')
numerical_data = innovations_df[['student_id', 'category', 'submission_date']].copy()
numerical_data['month'] = numerical_data['submission_date'].dt.month
numerical_data['day'] = numerical_data['submission_date'].dt.day
numerical_data['year'] = numerical_data['submission_date'].dt.year

# Set a clean professional theme
sns.set_theme(style="whitegrid", context="talk")

# Create the enhanced pairplot
pair_plot = sns.pairplot(
    numerical_data,
    hue='category',
    palette='viridis',             # beautiful scientific colormap
    diag_kind='kde',               # smooth curves on the diagonal
    plot_kws={'alpha': 0.7, 's': 80, 'edgecolor': 'k'},  # scatter transparency & borders
    height=3.2
)

# Add overall title and layout adjustments
pair_plot.fig.suptitle(
    'Relationships Between Submission Dates and Project Categories',
    fontsize=22, fontweight='bold', y=1.02
)
pair_plot.fig.tight_layout()

# Save high-resolution enhanced pair plot
pair_plot.savefig('Sample_Output/enhanced_pairplot_relationships.png', dpi=300, bbox_inches='tight')

plt.show()
print("Enhanced pair plot saved in 'Sample_Output' folder.")

# ---- Enhanced Visualization : Bar chart for Idea Submissions by Category ------------------


# Set a clean, modern style
sns.set_theme(style="whitegrid")

plt.figure(figsize=(19.2, 10.8))

# Sort categories by frequency for clarity
category_counts = innovations_df['category'].value_counts().sort_values(ascending=False)

# Create bar chart using Seaborn for better visuals
ax = sns.barplot(
    x=category_counts.index,
    y=category_counts.values,
    palette='crest',    # elegant blue-green gradient
    edgecolor='black'
)

# Add chart title and labels with better formatting
plt.title('Number of Idea Submissions by Category', fontsize=22, fontweight='bold', pad=25)
plt.xlabel('Category', fontsize=18)
plt.ylabel('Number of Submissions', fontsize=18)
plt.xticks(rotation=20, fontsize=14)
plt.yticks(fontsize=14)

# Add data labels on top of each bar
for p in ax.patches:
    ax.text(
        p.get_x() + p.get_width() / 2,
        p.get_height() + 0.5,
        int(p.get_height()),
        ha='center', va='bottom',
        fontsize=13, fontweight='bold', color='#2E4053'
    )

# Remove unnecessary spines for a cleaner look
sns.despine(left=True, bottom=True)

# Add a light dashed horizontal grid for readability
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Save high-quality version
plt.tight_layout()
plt.savefig('Sample_Output/enhanced_bar_chart_category.png', dpi=300, bbox_inches='tight')
plt.show()

# ---- Dark Theme Enhanced Visualization : Project Status Distribution ------------------


# Prepare data
status_counts = innovations_df['status'].value_counts()

# Set dark theme style
plt.style.use('dark_background')

# Define vibrant contrasting colors for dark mode
colors = sns.color_palette("Spectral", len(status_counts))

# Create figure
plt.figure(figsize=(14, 8), facecolor='#1e1e1e')

# Plot pie chart
wedges, texts, autotexts = plt.pie(
    status_counts,
    labels=status_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    textprops={'fontsize': 13, 'color': 'white'},
    wedgeprops={'edgecolor': '#1e1e1e', 'linewidth': 1.5}
)

# Style percentage labels
for autotext in autotexts:
    autotext.set_fontsize(13)
    autotext.set_fontweight('bold')
    autotext.set_color('white')

# Donut effect for modern look
centre_circle = plt.Circle((0, 0), 0.65, fc='#1e1e1e')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Title styling
plt.title(
    'Project Status Distribution (Dark Theme)',
    fontsize=22, fontweight='bold', color='white', pad=30
)

# Add a subtle legend with white text
plt.legend(
    status_counts.index,
    title='Project Status',
    loc='center left',
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=12,
    title_fontsize=14,
    facecolor='#1e1e1e',
    labelcolor='white',
    frameon=False
)

# Layout and save
plt.tight_layout()
plt.savefig('Sample_Output/enhanced_pie_chart_status_dark.png', dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
plt.show()

# ---- Enhanced Visualization : Trend Line for Submissions Over Time ----------------------

# Prepare the data
innovations_df['submission_date'] = pd.to_datetime(innovations_df['submission_date'], errors='coerce')
innovations_df['month'] = innovations_df['submission_date'].dt.to_period('M')
submission_trends = innovations_df.groupby('month').size().reset_index(name='count')
submission_trends['month'] = submission_trends['month'].astype(str)

# Set a clean, modern Seaborn theme
sns.set_theme(style="whitegrid")

plt.figure(figsize=(19.2, 10.8))

# Create a smooth trend line with markers
ax = sns.lineplot(
    data=submission_trends,
    x='month',
    y='count',
    marker='o',
    color='#1f77b4',
    linewidth=3,
    markersize=10
)

# Title and labels with professional formatting
plt.title('Trend of Innovation Submissions Over Time', fontsize=22, fontweight='bold', pad=25)
plt.xlabel('Month', fontsize=18)
plt.ylabel('Number of Submissions', fontsize=18)
plt.xticks(rotation=45, fontsize=13)
plt.yticks(fontsize=13)

# Add value labels for clarity
for x, y in zip(submission_trends['month'], submission_trends['count']):
    plt.text(x, y + 0.5, str(y), ha='center', fontsize=12, fontweight='bold', color='#2E4053')

# Add subtle background grid
plt.grid(axis='y', linestyle='--', alpha=0.6)
sns.despine(left=True, bottom=True)

# Highlight highest point
max_y = submission_trends['count'].max()
max_x = submission_trends.loc[submission_trends['count'].idxmax(), 'month']
plt.scatter(max_x, max_y, color='red', s=120, zorder=5)
plt.text(max_x, max_y + 1, f'Peak: {max_y}', color='red', fontsize=13, fontweight='bold', ha='center')

# Save high-quality chart
plt.tight_layout()
plt.savefig('Sample_Output/enhanced_trend_line_submissions.png', dpi=300, bbox_inches='tight')
plt.show()